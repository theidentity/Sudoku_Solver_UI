import subprocess
from subprocess import Popen,PIPE


def start():
	process = Popen('bash', shell=False, stdout=PIPE, stdin=PIPE, stderr=PIPE)
	process.stdin.write("python show_solving.py\n")
	return process

def terminate(process):
	process.terminate();

def restart(process=None):
	if process != None:
		terminate(process)
	return start()

def getContent(process):
	content = ""
	line = process.stdout.readline()
	return line
		
def prepareDict(line):
	numbers = line.split(',')
	numbers = [x.replace('0',' ') for x in numbers]
	board = {}

	k = 0
	for i in range(9):
		for j in range(9):
			name = ''.join(['c',str(i),str(j)])
			board[name] = numbers[k]
			k+=1

	return board


