from timer import Timer2
import sys
seconds = 0
def echoTime():
	global seconds
	seconds = seconds + 1
t = Timer2(1000, echoTime, [], True)
t.start()
print ('--Result--')
print (str( t.isRunning()))
t.stop()

sys.exit()
#print t.isRunning()

#print "\n"
