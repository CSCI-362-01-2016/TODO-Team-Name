from music import*
import sys
inary = sys.argv[1].split(' ')
note1 = Note(int(inary[0]),1)
note2 = Note(int(inary[1]),1)

phr = Phrase(note1)
phr.addNote(note2)
Mod.palindrome(phr)
phrList = phr.getNoteList()
pArray = []
for note in phrList:
	npitch = note.getPitch()
	pArray.append(npitch)
print('\n--Result--')
print(pArray)
print('--EndResult--')
sys.exit()
