num_grid=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [0]
    #this is grid having 4 rows and 4 columns
]
print(num_grid[0][0])#num_grid[row][column] so you can access the element by giving index number
for row in num_grid:
    for columnn in row:
        print(columnn)