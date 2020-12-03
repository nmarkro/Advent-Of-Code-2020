def parse_map():
    tobaggan_map = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            tobaggan_map.append(list(line.strip()))
    return tobaggan_map

def count_trees_by_slope(in_map, slope_x, slope_y):
    count = 0
    x = 0
    y = 0

    while True:
        if in_map[y][x] == "#":
            count += 1

        y += slope_y
        if y >= len(in_map):
            break

        x += slope_x
        x %= len(in_map[y])

    return count

tobaggan_map = parse_map()

# Part 1
print("Part 1 count: {}".format(count_trees_by_slope(tobaggan_map, 3, 1)))

# Part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
product = 1

for slope in slopes:
    product *= count_trees_by_slope(tobaggan_map, slope[0], slope[1])

print("Part 2 product: {}".format(product))
