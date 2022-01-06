class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS Solution
        # Time Complexity: O(N) where N is the number of pixels 
        # Space Complexity: O(N) size of the stack

        stack = [(sr, sc)] # stack used to store the position of pixel
        color = image[sr][sc] # the color of the pixel at (sr, sc)
        visited = set() # set used to store the position of pixels that have been visited
        
        R = len(image) # the number of rows
        C = len(image[0]) # the number of columns
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # the four directions aka. neighbors
        
        while stack: 
            currentPixel = stack.pop() # pop the last element in the stack
            
            if currentPixel not in visited: # if the current pixel has not been visited
                image[currentPixel[0]][currentPixel[1]] = newColor # change the color of the current pixel to newColor
                visited.add(currentPixel) # add the current pixel to the visited set
                    
                for i in directions: # for each direction
                    r = currentPixel[0] + i[0] # the row of the neighbor
                    c = currentPixel[1] + i[1] # the column of the neighbor
                    
                    if (r >= 0 and r < R) and (c >= 0 and c < C): # if the neighbor is within the range of the image
                        if image[r][c] == color: # if the color of the neighbor is the same as the color of the current pixel
                            stack.append((r, c)) # add the neighbor to the stack

        return image # return the image