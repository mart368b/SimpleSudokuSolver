from pprint import pprint

WIDTH = 9
HEIGHT = 9

BLOCK_WIDTH = int(WIDTH/3)
BLOCK_HEIGHT = int(HEIGHT/3)

def get_blanck_board() -> list:
    return [0 for i in range(0, WIDTH*HEIGHT)]

base_set = [set([i for i in range(1, 10)]) for j in range(0, WIDTH*HEIGHT)]

empty_set = set()

class Board:
    def __init__(self, board):
        self.board = board
        self.solver_board = self.get_solver_board()
        self.blanks = 0
        for v in board: 
            if v == 0: 
                self.blanks += 1
        self.lowest_blanks = WIDTH*HEIGHT
    
    def copy(self):
        return Board(self.board.copy())

    def __str__(self):
        lines = []
        for i in range(0, len(self.board)):
            lines.append(str(self.board[i]))
            if (i%3) == 2:
                lines.append(' ')
            if (i%27) == 26:
                lines.append('\n')
            if (i%9) == 8:
                lines.append('\n')
        return ' ' +  ' '.join(lines)
    
    @staticmethod
    def str_solver(solver):
        lines = []
        for i in range(0, len(solver)):
            lines.append(str(solver[i]))
            if (i%3) == 2:
                lines.append(' ')
            if (i%27) == 26:
                lines.append('\n')
            if (i%9) == 8:
                lines.append('\n')
        return ' ' +  ' '.join(lines)

    def get_solver_board(self) -> list:
        solver_board = [set([i for i in range(1, 10)]) if self.board[j] == 0 else empty_set for j in range(0, WIDTH*HEIGHT)]
        for i, v in enumerate(self.board):
            self.update_solver(solver_board, i, v)
        return solver_board
    
    @staticmethod
    def reset_solver(solver, i, v):
        solver[i] = set([i for i in range(1, 10)]) if v == 0 else empty_set

    @staticmethod
    def update_solver(solver_board, i, v):
        x = i%WIDTH
        y = int(i/HEIGHT)
        if not v == 0:
            solver_board[x + y*WIDTH].clear()
        for rx in range(0, WIDTH):
            solver_board[rx + y*WIDTH].discard(v)
        for ry in range(0, HEIGHT):
            solver_board[x + ry*WIDTH].discard(v)
        bx = int(x/(WIDTH/3)) * int(WIDTH/3)
        by = int(y/(HEIGHT/3)) * int(HEIGHT/3)
        for rx in range(bx, int(WIDTH/3) + bx):
            for ry in range(by, int(HEIGHT/3) + by):
                solver_board[rx + ry*WIDTH].discard(v)

    def is_solved(self):
        return self.blanks == 0

    def is_valid(self, i, a):
        x = i%WIDTH
        y = int(i/HEIGHT)
        if not self.board[i] == 0:
            raise KeyError('')
        for rx in range(0, WIDTH):
            ni = rx + y*WIDTH
            if not self.board[ni] == 0 and self.board[ni] == a:
                nx = ni%WIDTH
                ny = int(ni/HEIGHT)
                print(x, y, a, nx, ny, self.board[ni])
                print(self)
                print(self.str_solver(self.get_solver_board()))
                raise KeyError('')
        for ry in range(0, HEIGHT):
            ni = x + ry*WIDTH
            if not self.board[ni] == 0 and self.board[ni] == a:
                print(x, y, a)
                print(self)
                print(self.str_solver(self.get_solver_board()))
                raise KeyError('')
        bx = int(x/(WIDTH/3)) * int(WIDTH/3)
        by = int(y/(HEIGHT/3)) * int(HEIGHT/3)
        for rx in range(bx, int(WIDTH/3) + bx):
            for ry in range(by, int(HEIGHT/3) + by):
                ni = rx + ry*WIDTH
                if not self.board[ni] == 0 and self.board[ni] == a:
                    print(x, y, a)
                    print(self)
                    print(self.str_solver(self.get_solver_board()))
                    raise KeyError('')


    def solve(self) -> list:
        if self.is_solved():
            return []

        safe_changes = []
        for i, solver in enumerate(self.solver_board):
            posibilties = list(solver)
            if len(posibilties) == 1:
                safe_changes.append((i, self.board[i]))
                self.board[i] = posibilties[0]
                # print(' '*indent + '(' + str(i%WIDTH) + ', ' + str(int(i/HEIGHT)) + ') = ' + str(posibilties[0]))
                self.update_solver(self.solver_board, i, posibilties[0])
                self.blanks -= 1

        if self.is_solved():
            return []
            
        if len(safe_changes) > 0:
            return self.solve() + safe_changes
        else:
            sorted_board = sorted(enumerate(self.solver_board), key=lambda x: len(x[1]))
            for i, solver in sorted_board:
                if len(solver) > 1:
                    for a in list(solver):
                        old_value = self.board[i]
                        self.board[i] = a
                        self.update_solver(self.solver_board, i, a)
                        # print(' '*indent + '(' + str(i%WIDTH) + ', ' + str(int(i/HEIGHT)) + ') = ' + str(a))
                        self.blanks -= 1
                        unsafe_changes = self.solve()
                        unsafe_changes.append((i, old_value))
                        if self.is_solved():
                            return unsafe_changes
                        else:
                            if self.blanks <= self.lowest_blanks:
                                self.lowest_blanks = self.blanks
                            for j, v in unsafe_changes:
                                self.board[j] = v
                                self.blanks += 1
                            self.solver_board = self.get_solver_board()
            return []