from music import *
import sys
inary = sys.argv[1].split(' ')
#Create 2 note objects to add to phrase to perform palindrome function on.
note1 = Note(int(inary[0]), 1)
note2 = Note(int(inary[1]), 1)
#Create phrase and add both notes in order.
phr = Phrase(note1)
phr.addNote(note2)
Mod.repeat(phr, 2)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
print ('\n--Result--')
print pArray
print ('--EndResult--')
sys.exit()
