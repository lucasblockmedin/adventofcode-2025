with open('day3_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    banks = data.split('\n')
    print(banks)
    final = []
    for bank in banks:
        # WE get the first element from the list minus the last 12, that has to be our first element
        print('Bank, ', bank)
        best_joltage = ''
        idx = 0
        for i in range(11, -1, -1):
            print(i)
            if i == 0:
                bank_slice = bank[idx:]
            else:
                bank_slice = bank[idx:-i]
            print('Bank slice, ', bank_slice)
            print(bank_slice)
            element = max(bank_slice)
            print('Element, ', element)
            idx += bank_slice.index(element) + 1
            print('Index, ', idx)
            best_joltage += element
        print(best_joltage)
        final.append(int(best_joltage))
    print(final)
    print(sum(final))


