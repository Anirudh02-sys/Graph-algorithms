''' Code to compare avl and bst trees'''
from time import time


class Node:
    def __init__(self, data=None):
        self.key = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return root.height

    def balance(self, root):
        if root is None:
            return 0
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)

    def minValNode(self, root):
        if root is None or root.left is None:
            return root
        else:
            return self.minValNode(root.left)

    def leftRotate(self, node):
        x = node.right
        temp = x.left

        x.left = node
        node.right = temp

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))
        return x

    def rightRotate(self, node):
        x = node.left
        temp = x.right

        x.right = node
        node.left = temp

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))
        return x

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif root.key > data:
            root.left = self.insert(root.left, data)
        elif root.key < data:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        bf = self.balance(root)
        if bf > 1 and root.left.key > data:
            return self.rightRotate(root)

        elif bf > 1 and root.left.key < data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        elif bf < -1 and root.right.key < data:
            return self.leftRotate(root)

        elif bf < -1 and root.right.key > data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        if root:
            print(root.key, end=" ")
        if root.right is not None:
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)

    def delete(self, root, data):
        if root is None:
            return root
        elif root.key > data:
            root.left = self.delete(root.left, data)
        elif root.key < data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                lt = root.right
                root = None
                return lt
            if root.right is None:
                lt = root.left
                root = None
                return lt
            rgt = self.minValNode(root.right)
            root.key = rgt.key
            root.right = self.delete(root.right, rgt.key)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        bf = self.balance(root)
        if bf > 1 and self.balance(root.left) >= 0:
            return self.rightRotate(root)

        elif bf > 1 and self.balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        elif bf < -1 and self.balance(root.right) <= 0:
            return self.leftRotate(root)

        elif bf < -1 and self.balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


class BST:
    def binsert(self, root, data):
        if root is None:
            return Node(data)
        elif root.key > data:
            root.left = self.binsert(root.left, data)
        elif root.key < data:
            root.right = self.binsert(root.right, data)
        return root

    def binorder(self, root):
        if root.left is not None:
            self.binorder(root.left)
        if root:
            print(root.key, end=" ")
        if root.right is not None:
            self.binorder(root.right)

    def bpreorder(self, root):
        if root:
            print(root.key, end=" ")
        if root.left is not None:
            self.bpreorder(root.left)
        if root.right is not None:
            self.bpreorder(root.right)


def main():
    list = [45, 71, 89, 12, 67, 82, 1, 20, 22, 14, 90]

    x = AVL()
    root = None
    astart = time()
    for i in range(100):
        root = x.insert(root, i)
    aend = time()
    print("\nAVL PreORDER: ")
    x.preorder(root)
    for i in range(50):
        root = x.delete(root, i)
    print("\nAVL PreORDER after deletion: ")
    x.preorder(root)

    y = BST()
    broot = None
    start = time()
    for i in range(100):
        broot = y.binsert(broot, i)
    end = time()
    print("\nBST PreORDER: ")
    y.bpreorder(broot)
    print(f"\nTime taken for avl : {round(aend-astart,10)} ms")
    print(f"Time taken for bst : {round(end-start,10)}ms")


main()
