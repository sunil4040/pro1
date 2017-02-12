import requests
import sys

url_prefix = 'http://www.moneycontrol.com/news/'
end_number = 0
if len(sys.argv) == 2:
    end_number = int(sys.argv[1])
if end_number == 0:
    print('End number = 0. Exiting...')
    sys.exit(-1)
if end_number >= 100:
    print('End number >= 100. Exiting...')
    sys.exit(-1)

for i in range(10):
    for j in range(10):
        number = (i * 10 + j + 1)
        file_name = 'broker-research-reports-13-' + str(number) + '-next-' + str(i) + '.html'
        mc_url = url_prefix + file_name
        try:
            html = requests.get(mc_url)
        except requests.HTTPError as e:
            print('The server couldn\'t fulfill the request. {0}\nError code: {1}', mc_url, e.code)
        except requests.URLError as e:
            print('Failed to reach a server. {0}\nReason: ', mc_url, e.reason)
        else:
            file_name = "C:/data/temp/" + file_name
            mc_recommendation_file = open(file_name, 'w')
            mc_recommendation_file.write(html.text)
            mc_recommendation_file.close()
        if(end_number == number):
            break
    if(end_number == number):
        break