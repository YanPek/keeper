'''
Functions:

- saveValue(file, variable, value)
It will save the variable and value in the file. If the same variable already exists in the file, the value will be overwritten. The variable must not contain an assignment sign (=).

- getValue(file, variable)
Will return a value from a file by a variable.

Example:

    keeper.saveValue('eg.txt', 'x', 10)
    print(keeper.getValue('eg.txt', 'x'))

'''

class EqualityOperatorContent(Exception):
    pass

def saveValue(file, variable, value):
    if '=' in variable:
        equalIndex = variable.index("=")
        toError    = len(variable) - equalIndex - 1
        text       = '\nError: the variable must not contain an assignment sign (=)\n'
        errorText  = f'\n{" "*39}{"-"*equalIndex}^{"-"*toError}' + text
        error      = variable + errorText
        raise EqualityOperatorContent(error)
    saveThis = str(variable) + '=' + str(value) + '\n'
    try:
        with open(file) as f:
            textList = f.readlines()
    except:
        with open(file, 'w') as f:
            f.write(saveThis)
    else:
        if textList == ' ':
            with open(file, 'w') as f:
                f.write(saveThis)
        else:
            valuesList = []
            for i in textList:
                try:
                    valuesList.append(i[:i.index('=')])
                except:
                    pass
            if variable in valuesList:
                textList.pop(valuesList.index(str(variable)))
                textList.append(saveThis)
                with open(file, 'w') as f:
                    l = len(textList)
                    x = 0
                    while x < l:
                        f.write(textList[x])
                        x += 1
            else:
                textList.append(saveThis)
                with open(file, 'w') as f:
                    l = len(textList)
                    x = 0
                    while x < l:
                        f.write(textList[x])
                        x += 1

def getValue(file, variable):
    with open(file) as f:
        textList = f.readlines()
    valuesList = []
    for i in textList:
        try:
            valuesList.append(i[:i.index('=')])
        except:
            pass
    if variable in valuesList:
        line  = textList[valuesList.index(str(variable))]
        value = line[line.index('=') + 1:]
        return str(value)