from music import Phrase
import sys
phr = Phrase()
phr.addNote(int(sys.argv[1]), 1.0)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
print ('\n--Result--')
print pArray
print ('--EndResult--')
sys.exit()
