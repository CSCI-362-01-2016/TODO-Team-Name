from music import Phrase
import sys

phr = Phrase()
phr.addNote(127,1.0)
print ('--Result--')
print (phr.getNoteList())
print ('--EndResult--')
sys.exit()
