with open('day2_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split(',')
    print(data)
    data_ready = [x.split('-') for x in data]
    print(data_ready)
    invalid_ids = []
    for first, second in data_ready:
        rep_element = first[:len(first)//2] if len(first) > 1 else first
        print(first)
        print(second)
        while int(rep_element + rep_element) <= int(second):
            print('Rep element ', rep_element)
            print('Code element ', rep_element+rep_element)
            if int(rep_element + rep_element) >= int(first):
                invalid_ids.append(int(rep_element + rep_element))
            print(invalid_ids)
            rep_element = str(int(rep_element)+1)
    print(invalid_ids)
    print(sum(invalid_ids))