from functools import lru_cache

with open('day11_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    links = {}
    for line in data:
        left, right = line.split(':')
        links[left] = right.split()
    print(links)

    @lru_cache(maxsize=None)
    def find_outs(node, dac, fft):
        res = 0
        if node == 'out':
            if dac and fft:
                print('Found out with conditions')
                return 1
            else:
                return 0
        if node == 'dac':
            dac = True
        if node == 'fft':
            fft = True
        

        for new_node in links[node]:
            res += find_outs(new_node, dac, fft)
        
        return res
    
    print(find_outs('svr', False, False))
