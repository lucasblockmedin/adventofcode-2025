with open('day3_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    banks = data.split('\n')
    print(banks)
    final = []
    for bank in banks:
        max_element = max(bank)
        idx = bank.index(max_element)
        if idx+1 == len(bank):
            max_element2 = max(bank[:-1])
            print('First element, ', max_element2)
            final_el = str(max_element2) + str(max_element)
        else:
            max_element2 = max(bank[idx+1:])
            print('Second element, ', max_element2)
            final_el = str(max_element) + str(max_element2)
        final.append(int(final_el))
    print(final)
    print(sum(final))