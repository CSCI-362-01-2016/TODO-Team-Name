from music import Phrase
import sys
import time
phr = Phrase()
phr.addNote(int(sys.argv[1]), 1.0)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
time.sleep(1) 
print ('\n--Result--')
print phr.getSize()
print ('--EndResult--')
sys.exit()