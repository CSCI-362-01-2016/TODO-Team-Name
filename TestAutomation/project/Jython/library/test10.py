from music import Phrase
from music import Note
import sys
inary = sys.argv[1].split(' ')
phr = Phrase()
note1 = Note(int(inary[0]),1)
note2 = Note(int(inary[1]),1)
note3 = Note(int(inary[2]),1)
note4 = Note(int(inary[3]),1)
phr.addNote(note1)
phr.addNote(note2)
phr.addNote(note3)
phr.addNote(note4)
print ('\n--Result--')
print (phr.getSize())
print ('--EndResult--')
sys.exit()
