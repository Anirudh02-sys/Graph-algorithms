class Bin_tree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add(self, tree):
        self.children.append(tree)
        self.order += 1


class Bin_heap:
    def __init__(self):
        self.trees = []

    def enqueue(self, key):  # make singleton heap add tree merge
        singleton = Bin_heap()
        singleton.trees.append(Bin_tree(key))
        self.merge(singleton)

    def merge(self, other):
        self.trees.extend(other.trees)
        self.trees.sort(key=lambda tree: tree.order)
        i = 0
        while i < len(self.trees)-1:
            if self.trees[i].order == self.trees[i+1].order:
                if self.trees[i].key < self.trees[i+1].key:
                    self.trees[i].add(self.trees[i+1])
                    self.trees.pop(i+1)
                    i -= 1
                elif self.trees[i].key > self.trees[i+1].key:
                    self.trees[i+1].add(self.trees[i])
                    self.trees.pop(i)
                    i -= 1
            i += 1
    
    def peek(self):
        min = self.trees[0].key
        for i in range(len(self.trees)):
            if min > self.trees[i].key:
                min = self.trees[i].key
        print(min)

    def print_heap(self):
        print("head", end="")
        for i in self.trees:
            print("<-", i.key, [j.key for j in i.children],
                  f"({i.order})", end="")
        print()

    def extract_min(self):
        min = self.trees[0].key
        mintree = self.trees[0]
        for i in range(len(self.trees)):
            if min > self.trees[i].key:
                min = self.trees[i].key
                mintree = self.trees[i]
        self.trees.remove(mintree)
        temp = Bin_heap()
        temp.trees = mintree.children
        self.merge(temp)


def main():
    m = Bin_heap()
    m.enqueue(13)
    m.print_heap()
    m.enqueue(12)
    m.print_heap()
    m.enqueue(19)
    m.print_heap()
    m.enqueue(6)
    m.print_heap()
    m.enqueue(5)
    m.print_heap()
    m.enqueue(10)
    m.print_heap()
    m.peek()
    m.extract_min()
    m.print_heap()
    m.extract_min()
    m.print_heap()


main()
