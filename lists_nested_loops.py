
#  2 dimensional lists/ miltidimensional arrays
#  creating a grid (suduko, graphs)
#  list structure
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[1][2])

# nested for loops in order to parse two dimensional arrays
for row in number_grid:
    for col in row:
        print(col)

