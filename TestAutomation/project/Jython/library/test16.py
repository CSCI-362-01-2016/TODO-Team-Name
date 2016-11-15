from music import Phrase
from music import Note
import sys

phr = Phrase()
pitchList = [1,2,3]
phr.addChord(pitchList,5)
print ('\n--Result--')
print (phr.getNoteList())
print ('--EndResult--')
sys.exit()
