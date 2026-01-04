def print_grid(rows):
    for r in rows:
        print(r)

with open('day7_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print_grid(data)
    ray_positions = {data[0].index('S'): 1}
    print('Initial ray, ', ray_positions)
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
            new_rays = {}
            for ray, count in ray_positions.items():
                if ray in splitter_positions:
                    print('There is a hit at ', ray)
                    n_ray_1 = ray-1
                    n_ray_2 = ray+1
                    
                    if n_ray_1 >= 0:
                        new_rays[n_ray_1] = new_rays.get(n_ray_1, 0) + count
                    if n_ray_2 <= len(row):
                        new_rays[n_ray_2] = new_rays.get(n_ray_2, 0) + count
                else:
                    new_rays[ray] = new_rays.get(ray, 0) + count
            ray_positions = new_rays                
            print(ray_positions)
    print_grid(data)
    total_rays = sum(ray_positions.values())
    print(total_rays)


