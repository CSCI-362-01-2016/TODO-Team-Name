from music import Phrase
from music import Note
import sys

phr = Phrase()
inary = sys.argv[1].split(' ')
pitchList = [int(inary[0]),int(inary[1]),int(inary[2])]
phr.addChord(pitchList,5)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
print ('\n--Result--')
print pArray
print ('--EndResult--')
sys.exit()
