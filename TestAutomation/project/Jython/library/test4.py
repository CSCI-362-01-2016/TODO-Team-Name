from music import *
import time
import sys
#Create counting function and basic Timer2 object.
def echoTime():
   global seconds
   seconds = seconds + 1
t = Timer2(1000, echoTime, [],False)
t.start()
t.stop()
time.sleep(1)
print ('\n--Result--')
print (t.isRunning())
print ('--EndResult--')
sys.exit()