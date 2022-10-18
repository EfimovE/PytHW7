# import model_str
# string = model_str.calc_str

def operationStr (string):
    opSelect = {
        "*": lambda x, y: float(x) * float(y),
        "/": lambda x, y: float(x) / float(y),
        "+": lambda x, y: float(x) + float(y),
        "-": lambda x, y: float(x) - float(y)}
    
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    string = string.split()
    
    def deleteElement(string, i):
        string.pop(i + 1)
        string.pop(i)
    
    def operation(string, i, oper):
        if string[i] == oper:
            string[i - 1] = opSelect.get(oper)(float(string[i - 1]), float(string[i + 1]))
            deleteElement(string, i)
            return True
    
    example = ''.join(string)
    
    while len(string)>1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if operation(string, i, '*'): break
                if operation(string, i, '/'): break
    
        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if operation(string, i, '+'): break
                if operation(string, i, '-'): break
    
    # prfloat(f'{example}={string[0]}')
    return string[0]