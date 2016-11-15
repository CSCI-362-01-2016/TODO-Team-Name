from music import *
import time
import sys
def echoTime():
   global seconds
   seconds = seconds + 1
t = Timer2(1000, echoTime, [],True )
t.start()
time.sleep(1)
print ('\n--Result--')
print (t.getRepeat())
print ('--EndResult--')
t.stop()
sys.exit()