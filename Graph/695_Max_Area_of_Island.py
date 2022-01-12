# TODO: add comments
import collections 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        maxArea = 0
        visited = set()
        
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == 1:
                    maxArea = max(maxArea, BFS(i, j, visited, grid, R, C))
                    
        return maxArea

def BFS(r, c, visited, grid, R, C):
    queue = collections.deque()
    queue.append((r, c))
    area = 0
    
    while queue:
        r, c = queue.popleft()
        
        if (r,c) not in visited:
            visited.add((r,c))
            area += 1
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if (nr >= 0 and nr < R) and (nc >= 0 and nc < C):
                    if grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        
    return area
            