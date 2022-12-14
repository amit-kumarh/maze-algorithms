import matplotlib.pyplot as plt

def graph(points=[]):
    with open('demo_maze.txt', 'r') as f:
        grid = eval(f.read())

    for x, y in points:
        grid[x][y] = 2


    plt.pcolormesh(grid)
    plt.gca().set_aspect('equal')
    plt.xticks([]) # remove the tick marks by setting to an empty list
    plt.yticks([]) # remove the tick marks by setting to an empty list
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == '__main__':
    graph([(0, 0), (1, 0)])

