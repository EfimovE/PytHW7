import datetime

def logger_calc(str, result):
    dtime = f'{datetime.datetime.now()}'
    with open ('log_calc_str.txt', 'a', encoding='UTF-8') as file:
        file.write (f'{str} = {result} : {dtime} \n ')