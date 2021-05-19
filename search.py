from server import Board


def is_terminal(b: Board):
    for i in b.size ** 2:
        if b[i] == 0:
            return False
    return True
