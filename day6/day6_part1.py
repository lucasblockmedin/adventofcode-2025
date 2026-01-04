import re
import operator as op

ops = {
    '+': op.add,
    '*': op.mul,
}


with open('day6_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    operators = re.findall(r'[\+\-\*/]', data[-1])
    data = data[:-1]
    data = [list(map(int, re.findall(r'\d+', row))) for row in data if row]
    print(data)
    print(operators)
    res = 0
    for i in range(len(operators)):
        print(i)
        print(operators[i])
        operator_symbol = operators[i]
        if operator_symbol == '*':
            intres = 1
        else:
            intres = 0
        func = ops[operator_symbol]
        for row in data:
            intres = func(intres, row[i])
        print('Row result ', intres)
        res += intres
    print(res)


