from grid import create_grid
from astar import astar
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def animate_path(grid, path, start, goal):
    plt.ion()
    plt.figure(figsize=(6,6))

    for i in range(len(path)):
        plt.clf()
        plt.imshow(grid, cmap='gray')

        # full path (light)
        x_full = [p[1] for p in path]
        y_full = [p[0] for p in path]
        plt.plot(x_full, y_full, linestyle='--', alpha=0.3)

        # current path (blue)
        x = [p[1] for p in path[:i+1]]
        y = [p[0] for p in path[:i+1]]
        plt.plot(x, y, color='blue')

        # robot (yellow)
        current = path[i]
        plt.scatter(current[1], current[0], color='yellow', s=120)

        # start (green)
        plt.scatter(start[1], start[0], color='green', s=120)

        # goal (red)
        plt.scatter(goal[1], goal[0], color='red', s=120)

        # ✅ PERFECT LEGEND (fixed)
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Robot',
                   markerfacecolor='yellow', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Start',
                   markerfacecolor='green', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Goal',
                   markerfacecolor='red', markersize=10),
        ]
        plt.legend(handles=legend_elements, loc='upper right', frameon=True)

        plt.title("Autonomous Navigation (Moving Agent)")
        plt.tight_layout()
        plt.pause(0.3)

    plt.ioff()
    plt.show()

def main():
    while True:
        grid, start, goal = create_grid()

        path = astar(grid, start, goal)

        if path:
            print("Path found!")
            animate_path(grid, path, start, goal)
            break
        else:
            print("Retrying... No path found")

if __name__ == "__main__":
    main()
