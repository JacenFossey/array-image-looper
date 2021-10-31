# Defines the function to print the grid
def draw_pxlArt(grid, isOnSide):
    # If the 'image' is drawn sideways in the array, input 'True' as the second parameter. It changes the way the function loops through the array.
    if isOnSide == True:
        result_list = []
        column = 0
        length = int(len(grid)) - 1
        for column in range(len(grid[column])):
            row_str = ""
            for row in range(len(grid)):
                row_str += grid[row][column]
            result_list.append(row_str + "\n")
        print("".join(result_list[:length]))
    else:
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                print(grid[x][y], end="")
            print("")
