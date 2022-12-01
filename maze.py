import collections

ADJACENT = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Maze():
    def __init__(self):
        self.maze = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]
        self.start = (0,0)
        self.end = (2,2)

    def _getValidMoves(self, cell):
        neighbors = []
        for i, j in ADJACENT:
            row = cell[0] + i
            col = cell[1] + j
            if row not in range(0, self.end[0]+1) or col not in range(0, self.end[1]+1):
                continue

            if self.maze[row][col] == 0:
                neighbors.append((row, col))

        return neighbors

    def solve(self):
        visited = {}
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            curr = queue.pop()
            if curr == self.end:
                print("Reached the end")
                break

            moves = self._getValidMoves(curr)
            for move in moves:
                if move not in visited:
                    queue.append(move)
                    visited[move] = curr

        path = []
        path.append(visited[curr])
        while curr != self.start:
            path.append(curr := visited[curr])

        path = list(reversed(path))
        print(path)

if __name__ == '__main__':
    maze = Maze()
    maze.solve()
