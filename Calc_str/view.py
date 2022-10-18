# обеспечивает взаимодействие с пользователем
import logger

def error_value():
    logger.logger_calc('Ошибка ввода данных')
    return print ('Ошибка ввода данных')

def view_data (data):
    print (data)

def get_value():
    while True:
        try:
            return int(input ("Введите значение:  "))
        except:
            print ("Ошибка ввода данных, нужно повторить!")
    

def get_operation ():
    while True:
        a = input("Введите операцию: ")
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            print ("Ошибка ввода данных, нужно повторить!")
