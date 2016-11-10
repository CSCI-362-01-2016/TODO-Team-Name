from music import Phrase
from music import Note
import sys

phr = Phrase()
note1 = Note(10,1)
note2 = Note(20,2)
note3 = Note(30,3)
note4 = Note(40,4)
phr.addNote(note1)
phr.addNote(note2)
phr.addNote(note3)
phr.addNote(note4)
print ('--Result--')
print (phr.getEndTime() == 10.0)
print ('--EndResult--')
sys.exit()
