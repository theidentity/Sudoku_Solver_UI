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
		
