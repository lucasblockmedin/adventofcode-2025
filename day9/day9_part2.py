from itertools import combinations
import svgwrite
from shapely.geometry import LineString, MultiLineString, box
from shapely.ops import polygonize, unary_union


def polygon_from_segments(segments):
    """
    segments: iterable of ((x1,y1),(x2,y2)) line segments.

    Returns the largest enclosed Polygon formed by the segments.
    """
    lines = [
        LineString([a, b])
        for a, b in segments
        if a != b
    ]

    noded = unary_union(MultiLineString(lines))
    polys = list(polygonize(noded))

    if not polys:
        raise ValueError(
            "No polygons formed. Ensure segments form closed loops and share "
            "endpoints exactly (or properly intersect)."
        )

    return max(polys, key=lambda p: p.area)


def rectangle_from_opposite_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

def tile_rectangle_from_opposite_red_tiles(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    minx, maxx = sorted((x1, x2))
    miny, maxy = sorted((y1, y2))
    return box(minx - 0.5, miny - 0.5, maxx + 0.5, maxy + 0.5)

def draw_lines(points):
    all_x = []
    all_y = []
    parsed_points = []
    for point in points:
        left_coord, right_coord = point
        parsed_points.append((left_coord, right_coord))
        all_x.extend([left_coord[0], right_coord[0]])
        all_y.extend([left_coord[1], right_coord[1]])
    
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    
    canvas_size = 2000
    scale_x = canvas_size / (max_x - min_x) if max_x != min_x else 1
    scale_y = canvas_size / (max_y - min_y) if max_y != min_y else 1
    scale = min(scale_x, scale_y)
    
    dwg = svgwrite.Drawing('test.svg', size=(f'{canvas_size}px', f'{canvas_size}px'))
    dwg.viewbox(0, 0, canvas_size, canvas_size)
    
    for left, right in parsed_points:
        scaled_left = ((left[0] - min_x) * scale, (left[1] - min_y) * scale)
        scaled_right = ((right[0] - min_x) * scale, (right[1] - min_y) * scale)
        dwg.add(dwg.line(scaled_left, scaled_right, stroke=svgwrite.rgb(255, 0, 0, '%'), stroke_width=2))
    
    dwg.save()
    print(f"Bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
    print(f"Scale factor: {scale:.6f}")

with open('day9_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    pairs = list(combinations(data, 2))
    painting_points = []
    rectangles_points = []
    for combination in pairs:
        print(combination)
        left, right = combination
        left = left.split(',')
        right = right.split(',')

        if left[0] == right[0] or left[1] == right[1]:
            painting_points.append(((int(left[0]), int(left[1])), (int(right[0]), int(right[1]))))
        else:
            rectangles_points.append(((int(left[0]), int(left[1])), (int(right[0]), int(right[1]))))
    
    polygon = polygon_from_segments(painting_points)
    tile_region = polygon.buffer(0.5, join_style=2)
    print("tile region area:", tile_region.area)
    print("points:", len(data))
    print("painting segments:", len(painting_points))
    print("rect candidate pairs:", len(rectangles_points))
    print("polygon valid:", polygon.is_valid)
    print("polygon bounds:", polygon.bounds)
    print("polygon area:", polygon.area)
    max_covered_area = 0
    for rectangle_points in rectangles_points:
        rect = tile_rectangle_from_opposite_red_tiles(*rectangle_points)
        if tile_region.covers(rect):
            print('Rectangle covers polygon')
            if rect.area > max_covered_area:
                max_covered_area = rect.area
    print(max_covered_area)
    print(polygon.area)