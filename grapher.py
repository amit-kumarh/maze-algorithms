import matplotlib.pyplot as plt

def graph(path, points=[], queue=None):
    with open('demo_maze.txt', 'r') as f:
        grid = eval(f.read())

    for x, y in points:
        grid[x][y] = 2


    fig = plt.figure()
    plt.pcolormesh(grid)
    fig.gca().set_aspect('equal')
    # fig.gca().invert_yaxis()
    plt.xticks([]) # remove the tick marks by setting to an empty list
    plt.yticks([]) # remove the tick marks by setting to an empty list
    if queue:
        plt.xlabel(f"{[x for x in queue]}")
    fig.savefig(path, dpi=300)
    plt.close()

if __name__ == '__main__':
    graph([(0, 0), (1, 0)])

