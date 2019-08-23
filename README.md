# keeper

Functions:

- saveValue(file, variable, value)
It will save the variable and value in the file. If the same variable already exists in the file, the value will be overwritten. The variable must not contain an assignment sign (=).

- getValue(file, variable)
Will return a value from a file by a variable.

Example:

    keeper.saveValue('eg.txt', 'x', 10)
    print(keeper.getValue('eg.txt', 'x'))
