import operation
import view
import model
import logger

def button_click():
    value_a = view.get_value()
    value_operation = view.get_operation()
    value_b = view.get_value()
    model.init (value_a, value_b)
    if value_operation == '+':
        result = operation.summa()
    if value_operation == '-':
        result = operation.difference()
    if value_operation == '*':
        result = operation.multi()
    if value_operation == '/':
        result = operation.div()
    view.view_data(result)
    logger.logger_calc(value_a, value_b, value_operation, result)


