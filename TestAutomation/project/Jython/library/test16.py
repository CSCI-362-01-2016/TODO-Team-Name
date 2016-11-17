from music import Phrase
from music import Note
import sys

phr = Phrase()
inary = sys.argv[1].split(' ')
pitchList = [inary[0],inary[1],inary[2]]
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