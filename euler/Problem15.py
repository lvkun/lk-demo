#-------------------------------------------------------------------------------
# Name:        Problem 15
# Purpose:
#              Starting in the top left corner of a 22 grid, there are 6 routes 
#              (without backtracking) to the bottom right corner.
#              How many routes are there through a 2020 grid?
# Link:        http://projecteuler.net/index.php?section=problems&id=15
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def jc(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

def printGrid(grid):
    print "\n".join([' '.join([str(i) for i in l]) for l in grid])

def main():
    size = 21
    grid = [[0 for i in range(size)] for i in range(size)]
    grid[0][0]=0
    for i in range(1, size):
        grid[i][0] = 1
        grid[0][i] = 1

    for i in range(1, size):
        grid[i][i] = grid[i][i-1] + grid[i-1][i]

        for j in range(i+1, size):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]
            grid[j][i] = grid[j][i-1] + grid[j-1][i]

    printGrid(grid)
    print jc(40)/(jc(20)*jc(20))

    
if __name__ == '__main__':
    main()
