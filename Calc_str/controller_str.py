import operation_str
import view_str
import model_str
import logger_str

def button_click():
    value_str = view_str.get_calcStr()
    # print(value_str)
    model_str.init (value_str)
    result = operation_str.operationStr(value_str)
    view_str.view_data(result)
    logger_str.logger_calc(value_str, result)

# string = input('Введите выражение: ')
 
