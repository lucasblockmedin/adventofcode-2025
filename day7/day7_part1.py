def print_grid(rows):
    for r in rows:
        print(r)

with open('day7_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print_grid(data)
    ray_positions = {data[0].index('S')}
    print('Initial ray, ', ray_positions)
    ray_splits = 0
    for i, row in enumerate(data):
        print_grid(data)
        if i % 2 == 1:
            # This is a ray line, place rays
            for ray in ray_positions:
                data[i] = data[i][:ray] + '|' + data[i][ray+1:]
        else:
            # This is a line where splits can happen
            splitter_positions = [index for index, elem in enumerate(row) if elem=='^']
            print(splitter_positions)
            new_rays = set()
            for ray in ray_positions:
                if ray in splitter_positions:
                    print('There is a hit at ', ray)
                    ray_splits += 1
                    n_ray_1 = ray-1
                    n_ray_2 = ray+1
                    if n_ray_1 >= 0:
                        new_rays.add(n_ray_1)
                    if n_ray_2 <= len(row):
                        new_rays.add(n_ray_2)
                else:
                    new_rays.add(ray)
            ray_positions = new_rays                
            print(ray_positions)
    print(ray_splits)


