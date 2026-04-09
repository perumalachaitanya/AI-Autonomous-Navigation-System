import numpy as np
import random

def create_grid(size=20, obstacle_ratio=0.2):
    grid = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_ratio:
                grid[i][j] = 1

    start = (0, 0)
    goal = (size-1, size-1)

    grid[start] = 0
    grid[goal] = 0

    return grid, start, goal