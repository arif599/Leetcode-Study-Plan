class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # initize varibales
        visited = set()
        perimeter = 0
    
        # iterate over the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                   return bfs(grid, r, c, perimeter, visited)

def bfs(grid, r, c, perimeter, visited):
    import collections
    queue = collections.deque()
    queue.append((r,c))
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        currR, currC = queue.popleft()
        if (currR, currC) in visited: # we need to check if current row and col are not visited becasue there might be duplicates in the queue
            continue
        visited.add((currR, currC))
        perimeter += 4

        for dr, dc in directions:
            neighborR = currR + dr
            neighborC = currC + dc

            if (neighborR >=0 and neighborR < len(grid)) and (neighborC >=0 and neighborC < len(grid[0])): 
                if grid[neighborR][neighborC] == 1 and (neighborR, neighborC) not in visited:
                    queue.append((neighborR, neighborC)) 
                    perimeter -= 2
    return perimeter

# Time: O(r*c)
# Space: O(n)

