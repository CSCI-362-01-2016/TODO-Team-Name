from music import Phrase
from music import Note
import sys

phr = Phrase()
phrTest = Phrase()
pitchList = [1,2,3,4]
rhythmList = [1,1,1,1]
phr.addNoteList(pitchList, rhythmList)
phrTest.addNote(1,1)
phrTest.addNote(2,1)
phrTest.addNote(3,1)
phrTest.addNote(4,1)
print ('--Result--')
print (str(phr.getNoteList()) == str(phrTest.getNoteList()))
print ('--EndResult--')
sys.exit()
