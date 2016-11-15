from music import *
import sys
inary = sys.argv[1].split(' ')
#Create 2 note objects to add to phrase to perform palindrome function on.
note1 = Note(int(inary[0]), 1)
note2 = Note(int(inary[1]),1)
note3 = Note(int(inary[2]),1)
#Create phrase and add both notes in order.
phr = Phrase(note1)
phr.addNote(note2)
phr.addNote(note3)
Mod.palindrome(phr)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
   npitch = note.getPitch()
   pArray.append(npitch)
print ('\n--Result--')
print pArray
print ('--EndResult--')
sys.exit()
