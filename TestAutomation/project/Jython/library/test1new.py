from timer import Tiemr2
import sys
def main:
	seconds=0
	def echoTime():
		global seconds
		seconds = seconds + 1
	t = Tiemr2(1000,echoTime,[],True)
	t.start()
	if sys.argv[1]=='startTest':
		print(str(t.isRunning()))
	t.stop()
	return 'test'
#print t.isRunning()
#sys.exit(str(t.isRunning()))
#print "\n"
