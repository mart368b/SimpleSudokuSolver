from pprint import pprint
from board import Board

def run():
    board = Board()
    pprint(board.board)
    pprint(board.get_block(0, 0))

if __name__ == "__main__":
    run()