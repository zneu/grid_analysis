grid = [[1,1,2,4,1,7,1,7,6,9],\
        [1,2,5,3,9,1,1,1,9,1],\
        [7,4,5,1,8,1,2,0,0,4],\
        [1,4,1,1,1,1,1,1,8,5],\
        [9,0,0,0,0,0,1,1,9,8],\
        [7,4,2,1,8,2,2,2,9,7],\
        [7,4,2,1,7,1,1,1,0,5],\
        [3,4,5,3,4,5,9,1,0,9],\
        [0,0,5,1,1,1,9,7,7,7]]

print
print "Our grid *********************"

for i in grid:
        print i

# SIZE OF MATRIX ---------------
rows = len(grid)     # row num
cols = len(grid[0])  # col num
celNum = rows * cols  # cell num

print
print "Number of rows", rows
print "Number of cols", cols
print "Number of cells", celNum
print

grid_sum = 0
for row in grid:
    for column in row:
        grid_sum += column
print "The grid sum is equal to {}.".format(grid_sum)

print "The grid average is equal to {}.".format(grid_sum/celNum)

# similarly, calculate the min, max,
largestNum = 0
for row in grid:
    for column in row:
        if column > largestNum:
            largestNum = column
print "the largest value is {}.".format(largestNum)

smallestNum = 0
for row in grid:
    for column in row:
        if column < smallestNum:
            smalelstNum = column
print "the smallest value is {}.".format(smallestNum)

print "the range of values in the grid are min: {} to max: {}.".format(smallestNum, largestNum)

# USER SELECTED ROW -----------------
rowID = raw_input("What row would you like to know about (0 indexed)?\n> ")
rowID = int(rowID)
# If user input is greater than the len of the grid (-1 because we are 0
# indexed in python and user probably doesn't know) or less than the len of
# the grid then we can let them know that the idnex they chose was out of range.
if rowID > rows - 1 or rowID < 0:
    print "Row index out of range"
    print "Setting to default -> the 1st row"
    rowID = 0

selectedRow = grid[rowID]

print "row", rowID, "values:",
print selectedRow

#****** PUT YOUR CODE HERE ***********
# Display values for a column
# selected by the user
# (similar to rowID above);
columnID = raw_input("What column would you like to know about (0 indexed)?\n > ")
columnID = int(columnID)
if columnID > cols - 1 or columnID < 0:
    print "Row index out of range"
    print "Setting to default -> the 1st column"
    columnID = 0

for row in grid:
    print row[columnID]

# SELECTED ROW/COL -------------
print "What cell value (x,y) would you like to know about?"
inCol = raw_input("X value: ")  # X coord - user input
inCol = int(inCol)
inRow = raw_input("Y value: ")  # Y coord - user input
inRow = int(inCol)

if (inCol > cols - 1 or inCol < 0) or \
   (inRow > rows - 1 or inRow < 0):
    print "Cell coordinates out of range"
    print "Setting to default -> (0,0)"
    inCol = 0
    inRow = 0

selCell = grid[inRow][inCol]

print "cell (" + str(inRow) + "," + str(inCol) + ") value:",
print selCell
print

for index, row in enumerate(grid):
    print index, " : ", row
