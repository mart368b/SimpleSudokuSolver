class Board:
    def __init__(self):
        self.board = [[0. for i in range(0, 9)] for i in range(0, 9)]

    def get_block(self, x, y):
        return [self.board[y][x: x + 3] for i in range(y, y + 3)]

    def get_row(self, i: int) -> list:
        return self.board[i]
    
    def get_column(self, i: int) -> list:
        return [self.board[i][j] for j in range(0, 9)]

