class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        empty = 0
        start_r = 0
        start_c = 0

        # Find start and count walkable cells
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    empty += 1

                elif grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def dfs(r, c, remaining):

            # Reached the ending square
            if grid[r][c] == 2:
                if remaining == 0:
                    return 1
                return 0

            # Mark current square as visited
            grid[r][c] = -1

            paths = 0

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if grid[nr][nc] == 0:
                        paths += dfs(nr, nc, remaining - 1)

                    elif grid[nr][nc] == 2:
                        paths += dfs(nr, nc, remaining)

            # Backtrack: make current cell available again
            grid[r][c] = 0

            return paths

        return dfs(start_r, start_c, empty)