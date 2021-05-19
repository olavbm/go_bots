class Board:
    def __init__(self, size=9):
        self.size = size
        self.board = {}
        for i in range(size ** 2):
            self.board[i] = 0

    def __repr__(self):
        for i in range(self.size ** 2):
            print(self.board[i], end="")
            if (i + 1) % self.size == 0:
                print()


class Tree:
    def __init__(self, root):
        pass


class Node:
    def __init__(self, parent=None, child=None):
        self.white = 0
        self.black = 0
        self.child = children
        self.parent = parent
