# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=1130

class Grid:
    __grids = []
    __x_max = 0
    __y_max = 0

    def __init__(self, input):
        f = open(input, 'r')
        while True:
            counts = f.readline().split(' ')
            if int(counts[0]) == 0 and int(counts[1]) == 0:
                break

            grid = []
            for i in range(0, int(counts[0])):
                line = []
                l = f.readline()
                [line.append(c) for c in l if c != '\n']
                grid.append(line)
            self.__grids.append(grid)
        f.close()

    def solve(self):
        for i in range(0, len(self.__grids)):
            grid = self.__grids[i]
            print(f"Field #{i + 1}:")

            for y in range(0, len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x] == "*":
                        continue
                    self.__x_max = len(grid[y])
                    self.__y_max = len(grid)

                    grid[y][x] = self.__checkNeighbours(grid, x, y)

            for line in grid:
                st = ""
                for c in line:
                    st += c
                print(st)
            print()
        self.__x_max = -1
        self.__y_max = -1

    def __checkNeighbours(self, grid, x, y):
        counter = 0
        if self.__isInBoundary(x - 1, y - 1) and grid[y - 1][x - 1] == "*":
            counter += 1
        if self.__isInBoundary(x, y - 1) and grid[y - 1][x] == "*":
            counter += 1
        if self.__isInBoundary(x + 1, y - 1) and grid[y - 1][x + 1] == "*":
            counter += 1

        if self.__isInBoundary(x - 1, y) and grid[y][x - 1] == "*":
            counter += 1
        if self.__isInBoundary(x + 1, y) and grid[y][x + 1] == "*":
            counter += 1

        if self.__isInBoundary(x - 1, y + 1) and grid[y + 1][x - 1] == "*":
            counter += 1
        if self.__isInBoundary(x, y + 1) and grid[y + 1][x] == '*':
            counter += 1
        if self.__isInBoundary(x + 1, y + 1) and grid[y + 1][x + 1] == "*":
            counter += 1
        return str(counter)

    def __isInBoundary(self, x, y):
        return 0 <= x < self.__x_max and 0 <= y < self.__y_max


grid = Grid('input.txt')
grid.solve()
