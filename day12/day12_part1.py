shapes_raw = {} 
requirements = [] 

with open("day12_input.txt") as f:
    lines = f.read().splitlines()
 
cur = None
for s in lines:
    s = s.strip()
    if not s:
        continue

    if "x" in s and ":" in s and s.split(":", 1)[0].count("x") == 1:
        size, rest = s.split(":", 1)
        w_str, h_str = size.split("x", 1)
        key = (int(w_str), int(h_str))
        counts = [int(x) for x in rest.split()] if rest.strip() else []
        requirements.append((key, counts))
        continue

    if s.endswith(":") and s[:-1].isdigit():
        cur = int(s[:-1])
        shapes_raw[cur] = []
        continue
    shapes_raw[cur].append(s)

print("shapes_raw:", shapes_raw)
print("requirements:", requirements)
num_possible_to_fit = 0
num_needs_evaluating = 0
for grid in requirements:
    total_size = grid[0][0] * grid[0][1]
    print(total_size)
    num_shapes_to_fit = sum(grid[1])
    print(num_shapes_to_fit)
    
    # Impossible to fit
    if num_shapes_to_fit*7 > total_size:
        print("Impossible to fit")
    elif num_shapes_to_fit*9 < total_size:
        print("Possible to fit easily")
        num_possible_to_fit += 1
    else:
        print("Needs evaluating")
        num_needs_evaluating += 1
print(num_possible_to_fit, num_needs_evaluating)
