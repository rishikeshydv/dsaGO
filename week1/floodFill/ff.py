

from typing import List
from typing import List
class Solution:
    def __init__(self, sr: int, sc: int, newColor: int, image: List[List[int]]):
        self.sr = sr
        self.sc = sc
        self.newColor = newColor
        self.image = image
        self.row = len(self.image)
        self.col = len(self.image[0])
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.visited = set()

    def floodFill(self, sr: int, sc: int) -> List[List[int]]:
        if not self.image:
            return self.image
        self.dfs(sr, sc, self.image[sr][sc])
        return self.image

    def dfs(self, sr: int, sc: int, oldColor: int):
        if (sr < 0 or sr >= self.row or sc < 0 or sc >= self.col or self.image[sr][sc] != oldColor or (sr, sc) in self.visited):
            return
        self.image[sr][sc] = self.newColor
        self.visited.add((sr, sc))
        for direction in self.directions:
            self.dfs(sr + direction[0], sc + direction[1], oldColor)
    


input = [[1,1,1],[1,1,0],[1,0,1]]            
sol = Solution(1,1,2,input)
print(sol.floodFill(1,1)) # [[2,2,2],[2,2,0],[2,0,1]]

