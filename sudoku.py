import numpy as np


class Sudoku(object):
	"""class to store and solve Sudoku"""
	def __init__(self, puzzle_in):
		self.board = self.prepareBoard(puzzle_in)
		self.solvedBoard = None

	# -------------------HELPERS-------------------
	def prepareBoard(self,puzzle_in):
		board = map(int,str(puzzle_in))
		board = np.array(board)
		board = board.reshape(-1,9)
		if board.shape != (9,9):
			return None
		return board

	def printBoard(self,board):
		board = self.board
		for i,row in enumerate(board):
			row_output = ''.join([str(x) if x!=0 else " " for x in row])
			print ('{} {} {}|'*3).format(*row_output)
			if i%3==2:
				print '-'*19

	def serializeBoard(self,board):
		board = self.board
		numbers = board.flatten()
		numbers = [str(x).replace('0',' ') for x in numbers]
		return numbers
		
	# -------------------SOLVING-------------------
	def fillNext(self,board):
		X,Y = np.where(board==0)
		if X.size!=0 and Y.size!=0:
			return X[0],Y[0]
		return -1,-1

	def isCorrect(self,numbers):
		numbers = numbers[numbers>0].flatten()
		return np.unique(numbers).size == len(numbers)

	def isValidInsertion(self,i,j,n):
		self.board[i][j] = n
		
		rowOk = self.isCorrect(self.board[i,:])
		colOk = self.isCorrect(self.board[:,j])
		
		x,y = 3*(i/3),3*(j/3)
		squareOk = self.isCorrect(self.board[x:x+3,y:y+3])
		
		self.board[i][j]=0
		return rowOk and colOk and squareOk

	def solveBoard(self,i=0,j=0):
		i,j = self.fillNext(self.board)
		if i==-1:
			return True

		for n in range(1,10):
			if self.isValidInsertion(i,j,n):
				self.board[i][j] = n
				if self.solveBoard(i,j):
					return True
				self.board[i][j]=0

		return False

	def solve(self):
		if self.solveBoard():
			self.solvedBoard = self.board
		else:
			self.solvedBoard = None		

	# -------------------CHECKING-------------------
	def checkSolution(self):
		if type(self.solvedBoard) is not np.ndarray:
			print "Not a valid board"
			return False

		for i in range(9):
			if not (self.isCorrect(self.solvedBoard[i,:]) and self.isCorrect(self.solvedBoard[:,i])):
				return False

		for i in range(0,9,3):
			for j in range(0,9,3):
				if not self.isCorrect(self.solvedBoard[i:i+3,j:j+3]):
					return False

		return True

	def check(self):
		if self.checkSolution():
			print "correct"
		else:
			print "incorrect solution"


# s = Sudoku('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
# s.printBoard(s.board)
# s.solve()
# s.printBoard(s.solvedBoard)
# s.check()