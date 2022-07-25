from time import time
import copy
inf = 9999999999999999


class Graph:
    def __init__(self, g):
        self.g = g
        self.n = len(g)

    def print_graph(self):
        g = self.g
        n = self.n
        for i in range(n):
            print(" ", i, end="")
        print()
        for i in range(n):
            print(i, g[i])


class shortestPath(Graph):

    def minDistance(self, d, visited):
        min = inf
        min_index = 0
        for i in range(self.n):
            if d[i] < min and visited[i] == False:
                min = d[i]
                min_index = i
        return min_index

    def djikstra(self, s):
        g = self.g
        n = self.n
        d = [inf for _ in range(n)]
        visited = [False for _ in range(n)]
        d[s] = 0
        for _ in range(n):
            x = self.minDistance(d, visited)
            visited[x] = True
            for y in range(n):
                if g[x][y] > 0 and visited[y] == False and d[y] > d[x] + g[x][y]:
                    d[y] = d[x] + g[x][y]
        print("SSSP USing Djikstra")
        for i in range(n):
            print(i, " - ", d[i])

    def floydWarshall(self):
        g = self.g
        n = self.n
        for i in range(n):
            for j in range(n):
                if g[i][j] == 0 and i != j:
                    g[i][j] = inf
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])
        print("All Pair Shortest Path Graph")
        self.print_graph()

    def bellmanFord(self, s):
        g = self.g
        n = self.n
        e = []
        d = [inf for _ in range(n)]
        d[s] = 0
        for i in range(n):
            for j in range(n):
                if g[i][j] != 0:
                    e.append([i, j])
        for _ in range(n-1):  # relaxation
            for u, v in e:
                if d[v] > d[u] + g[u][v]:
                    d[v] = d[u] + g[u][v]
        print("SSSP USing Bellman Ford")
        for i in range(n):
            print(i, " - ", d[i])


def main():
    '''g = [[0, 28, 0, 0, 0, 10, 0],
         [28, 0, 16, 0, 0, 0, 14],
         [0, 16, 0, 12, 0, 0, 0],
         [0, 0, 12, 0, 22, 0, 18],
         [0, 0, 0, 22, 0, 25, 24],
         [10, 0, 0, 0, 25, 0, 0],
         [0, 14, 0, 18, 24, 0, 0]]'''
    g = [[0, 4, 2, 0, 0, 0],
         [4, 0, 1, 5, 0, 0],
         [2, 1, 0, 8, 10, 0],
         [0, 5, 8, 0, 2, 6],
         [0, 0, 10, 2, 0, 5],
         [0, 0, 0, 6, 5, 0],
         ]
    m = shortestPath(g)
    m.print_graph()
    m.djikstra(0)
    m.bellmanFord(0)
    m.floydWarshall()


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f'Took {end-start} seconds')
