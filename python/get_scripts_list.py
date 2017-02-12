def get_script_symbol(scrip, scripts_list):
    symbol = (scripts_list.loc[scripts_list.NAME_OF_COMPANY.str.startswith(scrip.upper())]).SYMBOL
    if len(symbol) == 1:
        return symbol.iloc[0]
    elif len(symbol) == 0:
        symbol = (scripts_list.loc[scripts_list.NAME_OF_COMPANY.str.startswith('THE ' + scrip.upper())]).SYMBOL
        if len(symbol) == 1:
            return symbol.iloc[0]
        return 'NA'
    else:
        return 'NA'