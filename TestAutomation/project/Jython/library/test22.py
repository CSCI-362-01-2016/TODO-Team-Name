from music import *
import sys
#Use input argument to create first note
note1 = Note(int(sys.argv[1]) ,1)
phr = Phrase(note1)
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
