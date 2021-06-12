class Board:
    def __init__(self, size=9):
        self.size = size
        self.board = numpy.zeros([self.size, self.size])

    def __repr__(self):
        print(self.board)


class Tree:
    def __init__(self, root):
        pass


class Node:
    def __init__(self, parent=None, child=None):
        self.white = 0
        self.black = 0
        self.child = children
        self.parent = parent
