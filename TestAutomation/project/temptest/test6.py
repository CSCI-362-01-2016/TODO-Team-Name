from music import Phrase
import sys

phr = Phrase()
phr.addNote(1,1.0)
print ('--Result--')
print (phr.getNoteList())
print ('--End Result--')
sys.exit()
