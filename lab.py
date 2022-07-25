inf = 99999999


class Graph:
    def __init__(self, g):
        self.g = g
        self.n = len(self.g)

    def print_graph(self):
        g = self.g
        print(" ", end="  ")
        for i in range(len(g)):
            print(i, end="  ")
        print()
        for i in range(len(g)):
            print(i, g[i])


class Flow(Graph):
    def __init__(self, g):
        super().__init__(g)
        trans = [[g[j][i] for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            if g[i] == [0]*self.n:
                self.sink = i
            if trans[i] == [0]*self.n:
                self.source = i
        print("Flow :", self.source, '->', self.sink)

    def DFS(self):
        g = self.g
        n = self.n
        stack = []
        stack.insert(0, self.source)
        x = 0
        while stack[-1] != self.sink and x+1 < n:
            i = stack[x]
            for j in range(n):
                if g[i][j] != 0 and j not in stack:
                    stack.insert(x+1, j)
                    break
                if g[i] == [0]*n:
                    return []
            x += 1
        return stack

    def max_flow(self):
        g = self.g
        n = self.n
        aug_path = self.DFS()
        print("Augmentation path :", aug_path)
        print("Current Graph:")
        self.print_graph()
        maxFlow = 0
        while len(aug_path) != 0:
            min = inf
            for i in range(len(aug_path)-1):  # here i find min weight for the aug path
                if g[aug_path[i]][aug_path[i+1]] < min:
                    min = g[aug_path[i]][aug_path[i+1]]
            maxFlow += min
            for i in range(len(aug_path)-1):
                g[aug_path[i]][aug_path[i+1]] -= min
            aug_path = self.DFS()
            if len(aug_path) != 0:
                print("Augmentation path :", aug_path)
                print("Current Graph:")
                self.print_graph()
            else:
                print("No more augumentation paths....")

        print("Max Flow :", maxFlow)


def main():

    g = [[0, 4, 3, 0, 0, 0],
         [0, 0, 0, 4, 0, 0],
         [0, 0, 0, 0, 6, 0],
         [0, 0, 3, 0, 0, 2],
         [0, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 0, 0]]
    m = Flow(g)

    m.max_flow()


main()
