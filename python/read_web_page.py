import string
from bs4 import BeautifulSoup
import get_scripts_list
import get_price_on_date
import sqlite3
import sys
import datetime

valid_actions = ('BUY', 'ACCUMULATE', 'HOLD', 'SELL', 'REDUCE', 'NEUTRAL')

def get_recmd_data(html_content, scripts_list, bhav_cons):
    full_soup = BeautifulSoup(html_content, 'html.parser')
    clearfix_tags = full_soup.find('ul', attrs={"class" : "nws_listing"}).find_all('div', attrs={"class" : "clearfix"})
    manual_updates = []
    recommendations = []
    recs_db = sqlite3.connect('C:/data/processed/recs.sqlite.db')
    cur = recs_db.cursor()
    for tag in clearfix_tags:
        title = str(tag.h2.a['title'])
        action = title.split()[0].strip().upper()
        scrip = string.capwords(title.split(';')[0][len(action)+1 : ].strip())
        words = title.split(':')
        target = words[0].split()[-1].replace(',', '')
        recommender = string.capwords(words[-1].strip())
        temp_date = str(tag.find('p', attrs={"class" : "MT2"}).contents[0]).replace("\n", "").split()
        report_date = ''.join([temp_date[-3], ' ', temp_date[-2], ' ', temp_date[-1][:-1]])
        temp_date = str(tag.find('p', attrs={"class": "nws_datetx MT5"}).contents[0])
        date_on_mc = temp_date[:temp_date.find('|')-1].strip()
        mc_url = str(tag.h2.a['href']).strip()
        rec_date_string = get_date_valid(report_date)
        if rec_date_string == 'INVALID_DATE':
            manual_updates.append([title, report_date, date_on_mc, mc_url])
            continue
        if action not in valid_actions:
            i = 0
            for valid_action in valid_actions:
                if action.find(valid_action) != -1:
                    process_rec(valid_action, scrip, target, recommender, rec_date_string, date_on_mc, mc_url,
                                title, recommendations, manual_updates, cur, recs_db, scripts_list, bhav_cons)
                    #     [valid_action, scrip, symbol, target, recommender, rec_date_string, date_on_mc, price_on_rec_date, mc_url],
                    #     [title, report_date, date_on_mc, mc_url])
                    break
                i = i + 1
            if i == len(valid_actions):
                manual_updates.append([title, report_date, date_on_mc, mc_url])
        else:
            process_rec(action, scrip, target, recommender, rec_date_string, date_on_mc, mc_url,
                        title, recommendations, manual_updates, cur, recs_db, scripts_list, bhav_cons)
            # process_rec(recommendations, manual_updates, symbol, recs_db, cur,
            #             [action, scrip, symbol, target, recommender, rec_date_string, date_on_mc, price_on_rec_date, mc_url],
            #             [title, report_date, date_on_mc, mc_url])
    cur.close()
    recs_db.commit()
    recs_db.close()
    return (recommendations, manual_updates)

def process_rec(action, scrip, target, recommender, rec_date_string, date_on_mc, mc_url,
                title, recommendations, manual_updates, cur, recs_db, scripts_list, bhav_cons):
    symbol = get_scripts_list.get_script_symbol(scrip, scripts_list)
    if symbol == 'NA':
        manual_updates.append([title, rec_date_string, date_on_mc, mc_url])
    else:
        price_on_rec_date = \
            float("{0:.2f}".format(get_price_on_date.get_price_for_date(symbol, rec_date_string, bhav_cons)))
        status = insert_rec_into_db(cur,
                [action, scrip, symbol, target, recommender, rec_date_string, date_on_mc, price_on_rec_date, mc_url])
        if status == 0:
            recommendations.append(
                [action, scrip, symbol, target, recommender, rec_date_string, date_on_mc, price_on_rec_date, mc_url])
        elif status == -1:
            cur.close()
            recs_db.rollback()
            recs_db.close()
            sys.exit(-1)

def insert_rec_into_db(cur, recm_rec):
    try:
        cur.execute("INSERT INTO RECS"
                    "(ACTION, COMPANY_NAME, SYMBOL, TARGET, RECOMMENDER, REC_DATE, DATE_ON_MC, PRICE_ON_REC_DATE, URL) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", recm_rec)
    except sqlite3.IntegrityError:
        print(recm_rec, 'Already present')
        return 1
    except sqlite3.Error as e:
        print("sqlite3 error: {0}".format(e))
        return -1
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return -1
    return 0

def get_date_valid(rec_date):
    try:
        datetime_object = datetime.datetime.strptime(rec_date, '%B %d, %Y')
        date_string = (datetime_object.strftime('%d-%b-%Y')).upper()
        return date_string
    except:
        return 'INVALID_DATE'