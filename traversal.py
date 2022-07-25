from cmath import e
from time import time


class Graph:
    def __init__(self, g):
        self.g = g
        self.n = len(self.g)

    def print_graph(self):
        g = self.g
        print(" ", end="  ")
        for i in range(len(g)):
            print(i+1, end="  ")
        print()
        for i in range(len(g)):
            print(i+1, g[i])

    def BFS(self):
        queue = []
        g = self.g
        n = self.n
        queue.append(1)
        x = 0
        while x < n:
            i = queue[x]
            for j in range(n):
                if g[i-1][j] == 1:
                    if j+1 not in queue:
                        queue.append(j+1)
            x += 1
        print(queue)

    def DFS(self):
        stack = []
        g = self.g
        n = self.n
        stack.insert(0, 1)
        x = 0
        while x < n:
            i = stack[x]
            for j in range(n):
                if g[i-1][j] == 1:
                    if j+1 not in stack:
                        stack.insert(x+1, j+1)

            x += 1
        print(stack)

    def topsort(self, spare=None, n=None, stack=None):
        g = self.g
        if spare is None:
            stack = []
            n = self.n
            spare = g[:]
        x = 0
        trans = [[spare[j][i] for j in range(n)] for i in range(n)]
        count = 0
        for i in range(len(trans)):
            if trans[i] == [0]*n and count == 0:
                addition = g.index(spare.pop(i))+1
                if addition in stack:
                    spare.insert(addition-1, g[addition-1])
                    x -= 1
                    count -= 1
                stack.insert(x, addition)
                x += 1
                count += 1
        print(spare)
        if len(stack) == self.n:
            print(stack)
        else:
            self.topsort(spare, len(spare), stack)


def main():
    '''g = [[0, 28, 0, 0, 0, 10, 0],
         [28, 0, 16, 0, 0, 0, 14],
         [0, 16, 0, 12, 0, 0, 0],
         [0, 0, 12, 0, 22, 0, 18],
         [0, 0, 0, 22, 0, 25, 24],
         [10, 0, 0, 0, 25, 0, 0],
         [0, 14, 0, 18, 24, 0, 0]]'''

    g = [[0, 1, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0]]

    m = Graph(g)
    # m.print_graph()
    print("BFS: ", end=" ")
    m.BFS()
    print("DFS: ", end=" ")
    m.DFS()

    gt = [[0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0],
          ]


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f'Took {end-start} seconds')
