import operator as op

ops = {
    '+': op.add,
    '*': op.mul,
}

def compute(nums, operator):
    new_nums = []
    for i in range(len(nums[0])-1, -1, -1):
        elem = ''
        for number in nums:
            elem += number[i]
        if elem.strip() == '':
            print('Empty element')
            continue
        else:
            new_nums.append(elem)
    func = ops[operator]
    if operator == '*':
        result = 1
        for num in new_nums:
            result = func(result, int(num))
        print('Result, ', result)
        return result
    else:
        result = 0
        for num in new_nums:
            result = func(result, int(num))
        print('Result, ', result)
        return result


with open('day6_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    operators = data[-1]
    numbers = data[:-1]
    print(operators)
    print(numbers)
    # We use the operator line to find the slices of our numbers
    last_cut = len(operators)
    res = 0
    for i in range(len(operators)-1, -1, -1):
        print(i)
        if operators[i] == '*' or operators[i] == '+':

            operator = operators[i]
            print(operator)
            nums = []
            for row in numbers:
                nums.append(row[i:last_cut])

            print(nums)
            last_cut = i
            print(compute(nums, operator))
            res += compute(nums, operator)
            
    print(res)


            
