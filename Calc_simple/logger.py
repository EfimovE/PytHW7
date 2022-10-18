import datetime

def logger_calc(num1, num2, operation, result):
    dtime = f'{datetime.datetime.now()}'
    with open ('log_calc.txt', 'a', encoding='UTF-8') as file:
        file.write (f'{num1} {operation} {num2} = {result} : {dtime} \n ')