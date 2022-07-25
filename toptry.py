
class Graph:
    def __init__(self, g):
        self.g = g
        self.n = len(g)
        self.list = []

    def adj_list(self):
        g = self.g
        al = {}
        for i in range(self.n):
            al[i] = []
        for i in range(self.n):
            for j in range(self.n):
                if g[i][j] != 0:
                    al[i].append(j)
        return al

    def print_graph(self):
        g = self.g
        n = self.n
        for i in range(n):
            print(" ", i, end="")
        print()
        for i in range(n):
            print(i, g[i])

    def top_sort(self, al=None):
        g = self.g
        n = self.n
        x = 0
        if al is None:
            al = self.adj_list()
        for i in al:
            if len(al[i]) == 0 and i not in self.list:
                self.list.append(i)
        for i in al.values():
            for j in self.list:
                if j in i:
                    i.remove(j)
        if len(self.list) != n:
            self.top_sort(al)
        else:
            print("TOP SORT : ", self.list[::-1])


def main():
    gt = [[0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0],
          ]

    g = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0],
         ]
    m = Graph(gt)

    m.top_sort()

    n = Graph(g)
    n.top_sort()


main()
