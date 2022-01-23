def orangesRotting(grid):
    # dimensions of the grid
    R = len(grid)
    C = len(grid[0])
    
    foundOranges = False
    empty = False
    
    import collections
    queue = collections.deque()
    rottenCount = 0
    freshCount = 0
    
    # iterate over the grind to find the rotten orange
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
                rottenCount += 1
            if grid[r][c] == 1:
                freshCount += 1

    if rottenCount > 0:
        return BFS(grid, (r, c), R, C, freshCount, rottenCount, queue)
    if freshCount:
        return -1

    return 0
                
def BFS(grid, source, R, C, freshCount, rottenCount, queue):
    visited = set()
    time = 0
    
    while queue:
        for i in range(rottenCount):
            currRow, currCol, currTime = queue.popleft()
            visited.add((currRow, currCol))
            time = currTime

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nRow = currRow + dr
                nCol = currCol + dc

                if (nRow >= 0 and nRow < R) and (nCol >= 0 and nCol < C):
                    if grid[nRow][nCol] == 1 and (nRow, nCol) not in visited:
                        freshCount -= 1
                        queue.append((nRow, nCol, currTime+1))


    return time if freshCount == 0 else -1
    

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))