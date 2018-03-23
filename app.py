

#!/usr/bin/env python

import os,sys,json
from bottle import route, run, static_file, template, view
from bottle import get, post, request
import terminal

@route('/css/<filename>')
def img_static(filename):
	return static_file(filename, root='./static/css')

@route('/img/<filename>')
def img_static(filename):
	return static_file(filename, root='./static/img')

@route('/js/<filename>')
def js_static(filename):
	return static_file(filename, root='./static/js')

@route('/fonts/<filename>')
def js_static(filename):
	return static_file(filename, root='./static/fonts')

process = terminal.start()


@route("/")
@view("sudoku")
def hello():
	global process

	content = ""
	while True:
		content = terminal.getContent(process)
		if '*' in content:
			break
		board = terminal.prepareDict(content)
		return dict(board)
	
	return complete()

@route("/complete")
@view("complete")
def complete():
		global process

		content = terminal.getContent(process)
		board = terminal.prepareDict(content)
		terminal.terminate(process)
		return dict(board)

# -------------------MAIN START----------------------------
if __name__ == "__main__":
	try:
		port = int(sys.argv[1])
	except:
		port = 5000
		
	port = int(os.environ.get("PORT", port))
	run(
	host='localhost',
	port=port,
	debug=True,
	reloader = True
	)
# -------------------MAIN END----------------------------
