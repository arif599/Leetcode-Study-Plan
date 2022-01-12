import collections 

def numIslands(grid):
    # dimentions of grid
    R = len(grid) # number of rows
    C = len(grid[0]) # number of columns

    islandCounter = 0 # number of islands
    visited = set() # set of visited nodes
    
    for i in range(R):
        for j in range(C):
            if (i,j) not in visited and grid[i][j] == "1": # if node is not visited and is an island
                islandCounter += BFS(i, j, R, C, visited, grid) # perform BFS on that node    
    
    return islandCounter
                    
def BFS(r, c, R, C, visited, grid):
    queue = collections.deque() # queue of nodes to visit
    queue.append((r, c)) # add node to queue

    while queue: # while queue is not empty
        row, col = queue.popleft() # get node from queue

        if (row, col) not in visited: # if node is not visited
            visited.add((row,col)) # add node to visited set

            # visit its neighbors
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left

            for x, y in direction: # for each direction in direction list
                r = row + x # row of neighbor
                c = col + y # column of neighbor

                # check if r, c are within the bounds of the grind and if the node is an island
                if (r >= 0 and r < R) and (c >= 0 and c < C) and grid[r][c] == "1":
                    queue.append((r, c)) # add neighbor to queue
                    
    return 1 # return 1 for each island

print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))