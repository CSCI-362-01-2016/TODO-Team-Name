from Timer import Timer

seconds = 0
def echoTime():
	global seconds
	print seconds
	seconds = seconds + 1
t = Timer(1000, echoTime, [], True)
t.start()
