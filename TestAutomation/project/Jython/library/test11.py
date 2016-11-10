from music import Phrase
from music import Note
import sys

phr = Phrase()
note1 = Note(10,1)
note2 = Note(20,1)
note3 = Note(30,1)
note4 = Note(40,1)
phr.addNote(note1)
phr.addNote(note2)
phr.addNote(note3)
phr.addNote(note4)
phr.empty()
print ('--Result--')
print (phr.getSize())
print ('--EndResult--')
sys.exit()
