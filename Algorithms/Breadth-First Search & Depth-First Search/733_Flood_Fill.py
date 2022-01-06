class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS
        stack = [(sr, sc)] # stack used to store the position of pixel
        color = image[sr][sc]
        visited = set()
        
        while stack:
            currentPixel = stack.pop()
            
            if currentPixel not in visited:
                image[currentPixel[0]][currentPixel[1]] = newColor
                visited.add(currentPixel)

                # add neighbors of pixel (4-directionally)
                if currentPixel[0]+1 < len(image) and image[currentPixel[0]+1][currentPixel[1]] == color:
                    # up direction
                    stack.append((currentPixel[0]+1, currentPixel[1]))

                if currentPixel[0]-1 >= 0 and image[currentPixel[0]-1][currentPixel[1]] == color:
                    # down direction
                    stack.append((currentPixel[0]-1, currentPixel[1]))

                if currentPixel[1]-1 >= 0 and image[currentPixel[0]][currentPixel[1]-1] == color:
                    # left direction
                    stack.append((currentPixel[0], currentPixel[1]-1))

                if currentPixel[1]+1 < len(image[0]) and image[currentPixel[0]][currentPixel[1]+1] == color:
                    # right direction
                    stack.append((currentPixel[0], currentPixel[1]+1))

        return image