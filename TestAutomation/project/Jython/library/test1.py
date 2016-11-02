from Timer import Timer
import sys
seconds = 0
def echoTime():
	global seconds
	seconds = seconds + 1
t = Timer(1000, echoTime, [], True)
t.start()
print "\n" +str( t.isRunning())
t.stop()
print t.isRunning()
sys.exit(str(t.isRunning()))

