import timeit
import numpy as np
from sudoku import Sudoku

puzzles = open('questions/ques.txt').read().split('\n')


times = []
for puzzle in puzzles[:2]:
	print puzzle
	s = Sudoku(puzzle)
	s.printBoard(s.board)
	
	start_time = timeit.default_timer()
	s.solve()
	elapsed = timeit.default_timer() - start_time
	
	s.printBoard(s.solvedBoard)
	s.check()

	print ('Solved in : {} sec').format(elapsed)
	times.append(elapsed)

print('Average time taken : {} sec').format(np.mean(elapsed))
	
