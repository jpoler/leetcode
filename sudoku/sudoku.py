import pprint
from copy import deepcopy
import functools
import math

from operator import add

empty_square = "."

class Solution:
    def solveSudoku(self, board):
        listified = [list(s) for s in board]
        s = Sudoku(listified)
        s.backtrack_dfs([], "")
        for i, row in enumerate(s.problem):
            board[i] = "".join(row)


board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

class Point:
    def __init__(self, value, row, col):
        self.value = value
        self.row, self.col = row, col

    def __repr__(self):
        return "Point < v: {}, r: {}, c: {} >".format(self.value, self.row, self.col)

class Backtrack(object):
    def __init__(self, problem):
       self.problem = problem
       self.solutions = []
       self.finished = False

    def backtrack_dfs(self, a, inp):
        if self.is_a_solution(a):
            self.solutions.append(deepcopy(self.problem))

        else:
            candidates = self.construct_candidates(a, inp)
            if candidates is None:
                return
            for c in candidates:
                a.append(c)
                self.make_move(a, inp)
                self.backtrack_dfs(a, inp)
                if self.finished:
                    return
                else:
                    self.unmake_move(a, inp)
                    a.pop()

    def make_move(self, a, inp):
        raise NotImplementedError("Make move")

    def unmake_move(self, a, inp):
        raise NotImplementedError("Unmake move")

    def construct_candidates(self, a, inp):
        raise NotImplementedError("Construct Candidates")

    def is_a_solution(self, a):
        raise NotImplementedErrror("Is a solution")

class Sudoku(Backtrack):



    def __init__(self, *args, **kwargs):
        super(Sudoku, self).__init__(*args, **kwargs)
        self.dim = len(self.problem)
        self.box_dim = int(math.sqrt(self.dim))
        self.all_moves = set(str(i) for i in range(1, self.dim+1))
        self.row_constraints = [self.build_row_constraints(i) for i in range(self.dim)]
        self.col_constraints = [self.build_col_constraints(i) for i in range(self.dim)]
        self.box_constraints = [self.build_box_constraints(i) for i in range(self.dim)]
        self.squares = self.dim * self.dim
        self.full_squares = functools.reduce(add, map(lambda x: self.dim - x.count(empty_square), self.problem), 0)
        self.moves = [Point(None, None, None) for _ in range(self.squares)]

    def get_box(self, row, col):
        return ((row // self.box_dim) * self.box_dim) + (col // self.box_dim)

    def get_box_row_and_col(self, box):
        row = (box // self.box_dim)*self.box_dim
        col = (box % self.box_dim)*self.box_dim
        return row, col

    def build_box_constraints(self, box):
        constraints = set()
        row, col = self.get_box_row_and_col(box)
        for i in range(row, row+self.box_dim):
            for j in range(col, col+self.box_dim):
                if self.problem[i][j] != empty_square:
                    constraints.add(self.problem[i][j])
        return constraints

    def build_col_constraints(self, col):
        constraints = set()
        for i in range(0, self.dim):
            if self.problem[i][col] != empty_square:
                constraints.add(self.problem[i][col])
        return constraints

    def build_row_constraints(self, row):
        constraints = set()
        for i in range(0, self.dim):
            if self.problem[row][i] != empty_square:
                constraints.add(self.problem[row][i])
        return constraints

    def find_available_moves(self, row, col):
        box_const = self.box_constraints[self.get_box(row, col)]
        row_const = self.row_constraints[row]
        col_const = self.col_constraints[col]
        const = box_const.union(row_const).union(col_const)


        return self.all_moves - const

    def find_most_constrained(self):
        most_row = None
        most_col = None
        most_constrained = [None]*(self.dim+1)
        for row in range(self.dim):
            for col in range(self.dim):
                if self.problem[row][col] == empty_square:
                    cell_constraints = self.find_available_moves(row, col)
                    if len(cell_constraints) != 0 and len(cell_constraints) < len(most_constrained):
                        most_row = row
                        most_col = col
                        most_constrained = cell_constraints
        return most_row, most_col
        
    def is_a_solution(self, a):
        if self.full_squares >= self.squares:
            self.finished = True
            return True
        return False

    def make_move(self, a, inp):
        p = a[-1]
        self.problem[p.row][p.col] = p.value
        self.box_constraints[self.get_box(p.row, p.col)].add(p.value)
        self.row_constraints[p.row].add(p.value)
        self.col_constraints[p.col].add(p.value)
        self.full_squares += 1

    def unmake_move(self, a, inp):
        p = a[-1]
        self.problem[p.row][p.col] = empty_square
        
        self.full_squares -= 1
        self.box_constraints[self.get_box(p.row, p.col)].remove(p.value)
        self.row_constraints[p.row].remove(p.value)
        self.col_constraints[p.col].remove(p.value)
        self.full_squares -= 1

    def next_square(self):
        return self.find_most_constrained()

    def construct_candidates(self, a, inp):
        row, col = self.next_square()
        if row is None or col is None:
            return
        
        possible_values = self.find_available_moves(row, col)
        return [Point(val, row, col) for val in possible_values]
        

if __name__ == '__main__':
    s = Solution()
    s.solveSudoku(board)
    print(board)
