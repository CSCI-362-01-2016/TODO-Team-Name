from music import *
import sys

#Create 2 note objects to add to phrase to perform palindrome function on.
note1 = Note(sys.argv[1], 1)
note2 = Note(sys.argv[2], 1)
#Create phrase and add both notes in order.
phr = Phrase(note1)
phr.addNote(note2)
Mod.palindrome(phr)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
print ('--Result--')
print pArray
print ('--EndResult--')
sys.exit()
