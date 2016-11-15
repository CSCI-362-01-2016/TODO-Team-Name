from music import Note
import sys
#Create note using music library constants. 
note1 = Note(int(sys.argv[1]) ,1)
print ('\n--Result--')
print (note1.getPitch())
print ('--EndResult--')
sys.exit()
