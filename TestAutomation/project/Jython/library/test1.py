from timer import Timer2
import sys
seconds = 0
def echoTime():
	global seconds
	seconds = seconds + 1
t = Timer2(1000, echoTime, [], True)
t.start()
if sys.argv[1]=='startTest':
	print (str( t.isRunning()))
t.stop()

sys.exit('test')
#print t.isRunning()

#print "\n"
