from music import Phrase
import sys
import time
phr = Phrase()
inary = sys.argv[1].split(' ')
phr.addNote(int(inary[0]), 1.0)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
time.sleep(1) 
print ('\n--Result--')
print pArray
print ('--EndResult--')
sys.exit()