from time import time
import copy
inf = 9999999999999999


class Graph:
    def __init__(self, g):
        self.g = g  # adj matrix
        self.n = len(g)  # n = 7

    def print_graph(self):
        g = self.g
        n = self.n
        for i in range(n):
            print(" ", i, end="")
        print()
        for i in range(n):
            print(i, g[i])


class MST(Graph):
    def __init__(self, g):
        Graph.__init__(self, g)
        self.disjoint = []
        self.t = []  # prims
        self.k = []  # prims
        self.tk = []  # kruskals

    def Prims(self, x):
        t = []  # initial
        s = []
        s.append(x)  # x=0
        g = self.g
        n = self.n
        while len(t) < n-1:
            min = []
            min_val = inf
            for i in s:
                for j in range(n):
                    if g[i][j] < min_val and g[i][j] != 0 and j not in s:
                        min = [i, j]  # [0,1] [0,5]
                        min_val = g[i][j]  # [0,5] ->10<28
            t.append(min)
            s.append(min[1])

        self.t = t
        self.s = s

    def make_sets(self):  # [[0,1,3],[2]]
        disjoint = self.disjoint
        for i in range(self.n):
            disjoint.append([i])

    def find(self, x):  # returns set of the stuff we want to find and index
        disjoint = self.disjoint
        for i in range(len(disjoint)):
            if x in disjoint[i]:
                return disjoint[i], i

    def union(self, a, b):
        disjoint = self.disjoint
        x, x_index = self.find(a)
        y, y_index = self.find(b)
        if x == y:
            return -1  # informing there is a cycle
        else:
            if x[0] < y[0]:  # parent of the list
                for i in y:
                    disjoint[x_index].append(i)
                disjoint.pop(y_index)
            else:
                for i in x:
                    disjoint[y_index].append(i)
                disjoint.pop(x_index)
            return 0

    def Kruskals(self):
        g = self.g
        n = self.n
        t = []
        self.make_sets()
        temp = []

        for i in range(n):
            for j in range(n):
                if g[i][j] != 0 and [[j, i], g[i][j]] not in temp:
                    temp.append([[i, j], g[i][j]])  # temp[i][1] = edge weight
        for i in range(len(temp)-1):  # bubble sort
            for j in range(len(temp)-i-1):
                if temp[j][1] > temp[j+1][1]:
                    temp[j], temp[j+1] = temp[j+1], temp[j]
        count = 0
        for i in temp:
            x = self.union(i[0][0], i[0][1])
            if x == 0:
                count += 1
                t.append(i)
            if count == self.n-1:
                break

        self.tk = t


def main():
    g = [[0, 28, 0, 0, 0, 10, 0],  # 0
         [28, 0, 16, 0, 0, 0, 14],  # 1
         [0, 16, 0, 12, 0, 0, 0],  # 2
         [0, 0, 12, 0, 22, 0, 18],
         [0, 0, 0, 22, 0, 25, 24],
         [10, 0, 0, 0, 25, 0, 0],
         [0, 14, 0, 18, 24, 0, 0]]  # 6
    k = 0.0
    p = 0.0
    m = MST(g)
    m.print_graph()
    for i in range(1000):
        m = MST(g)
        startp = time()
        m.Prims(0)  # parameter: start vertex
        endp = time()
        startk = time()
        m.Kruskals()
        endk = time()
        k += endk-startk
        p += endp-startp
    print("Mst using Prims : ")
    print("T :", m.t, "\nS :", m.s)
    print("Mst using Kruskals : ")
    print("T :", m.tk)
    print('Prims Took %.15f seconds' % (p/1000))
    print('Kruskals Took %.15f seconds' % (k/1000))


if __name__ == '__main__':
    main()
