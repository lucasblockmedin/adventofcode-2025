with open('test2.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split(',')
    print(data)
    data_ready = [x.split('-') for x in data]
    print(data_ready)
    invalid_ids = []
    for first, second in data_ready:
        print(first)
        print(second)
        for multiple in range(2, len(second)+1):
            print('MULTIPLE, ', multiple)
            units = len(second)//multiple
            print('Units, ', units)
            first_elem = int('1' + '0'*(units-1))
            last_elem = int('9' + '9'*(units-1))
            print('First elem ', first_elem)
            print('Last elem ', last_elem)

            for elem in range(first_elem, last_elem+1):
                elem_check = str(elem)*(multiple)
                print('Checking, ', elem_check)
                if int(elem_check) >= int(first) and int(elem_check)<= int(second):
                    invalid_ids.append(int(elem_check))
    print(len(invalid_ids))
    print(invalid_ids)
    print(sum(set( invalid_ids)))
    