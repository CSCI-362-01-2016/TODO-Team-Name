from music import Note
import sys
#Create note using MIDI scale 0-127. Duration of 1 for quarter note.
note1 = Note(int(sys.argv[1]),1)
print ('\n--Result--')
print (note1.getPitch())
print ('--EndResult--')
sys.exit()
