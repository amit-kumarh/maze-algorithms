import collections

ADJACENT = [1, 0, -1]

class Maze():
    def __init__(self):
        self.maze = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]
        self.start = (0,0)
        self.end = (2,2)

    def _getValidMoves(self, cell):
        neighbors = []
        for i in ADJACENT:
            for j in ADJACENT:
                if i == j == 0:
                    continue

                row = cell[0] + i
                col = cell[1] + j
                if i not in range(0, self.end[0]) or j not in range(0, self.end[1]):
                    continue

                print(row, col)
                if self.maze[row][col] == 0:
                    neighbors.append((row, col))

        return neighbors

    def solve(self):
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            curr = queue.pop()
            if curr == self.end:
                print("Reached the End")
                break

            moves = self._getValidMoves(curr)
            for move in moves:
                queue.append(move)

if __name__ == '__main__':
    maze = Maze()
    maze.solve()
