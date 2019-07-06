def get_blanck_board() -> list:
    return [[None for i in range(0, 9)] for i in range(0, 9)]

def get_solver_board() -> list:
    return [[set([i for i in range(0, 10)]) for i in range(0, 9)] for i in range(0, 9)]

class Board:
    def __init__(self, board = get_blanck_board()):
        self.board = board
        self.counter = 0
        self.solver_board = get_solver_board()
        self.update_solver()

    def update_solver(self):
        for y, (row, s_row) in enumerate(zip(self.board, self.solver_board)):
            for x, cell in enumerate(row):
                if not cell == None:
                    self.solver_board[y][x] = None
                    block = self.get_block(x, y)
                    self.get_column(x)

    def get_block(self, x, y):
        block = []
        for i in range(y, y + 3):
            block += self.board[i][x: x + 3]
        return block

    def get_row(self, y: int) -> list:
        return self.board[y]
    
    def get_column(self, x: int) -> list:
        return [self.board[y][x] for y in range(0, 9)]
    
