from music import *
import time
import sys
def echoTime():
   global seconds
   seconds = seconds + 1
t = Timer2(1000, echoTime, [],True )
t.setDelay(sys.argv[1])
print ('\n--Result--')
print (t.getDelay())
print ('--EndResult--')
t.stop()
sys.exit()