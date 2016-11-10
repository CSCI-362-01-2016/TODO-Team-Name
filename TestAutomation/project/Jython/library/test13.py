from music import Phrase
from music import Note
import sys

phr = Phrase()
note1 = Note(10,5)
phr.addNote(note1)
print ('--Result--')
print (phr.getEndTime() == 5.0)
print ('--EndResult--')
sys.exit()
