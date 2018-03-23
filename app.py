

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
def hello():
	global process

	content = ""
	k = 0
	while True:
		k += 1
		content = terminal.getContent(process)
		if '*' in content:
			return complete()
		else:
			if k%1 == 0:
				board = terminal.prepareDict(content)
				return template('sudoku',dict(board))


@route("/complete")
def complete():
		global process
		content = terminal.getContent(process)
		board = terminal.prepareDict(content)
		terminal.terminate(process)
		return template('complete',dict(board))

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
	# quiet = True
	)
# -------------------MAIN END----------------------------
