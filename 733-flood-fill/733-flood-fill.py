class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(sr, sc)]
        visited = {(sr, sc)}
        color = image[sr][sc]
        while q:
            x, y = q.pop()
            image[x][y] = newColor
            for dirx, diry in directions:
                tx, ty = x + dirx, y + diry
                if 0 <= tx < m and 0 <= ty < n and image[tx][ty] == color and (tx, ty) not in visited:
                    q.append((tx, ty))
                    visited.add((tx, ty))
        return image