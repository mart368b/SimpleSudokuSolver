from pprint import pprint
from board import Board

def run():
    board = Board( board = [
        [None,None,5,7,None,None,None,None,None], 
        [4,1,7,None,None,None,None,None,8], 
        [2,3,None,None,None,None,None,None,7], 
        [None,None,None,8,None,None,None,2,6], 
        [9,None,None,None,7,1,3,8,4], 
        [None,4,None,5,None,None,1,None,None], 
        [None,None,None,3,None,None,8,None,None], 
        [None,6,8,None,None,None,None,1,None], 
        [5,None,4,1,8,None,7,9,3]
    ])
    pprint(board.board)
    pprint(board.solver_board)

if __name__ == "__main__":
    run()