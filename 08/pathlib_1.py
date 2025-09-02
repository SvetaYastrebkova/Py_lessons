''''
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent
NEW_FILE_PATH = PROJECT_ROOT.join("text1.txt")

ACCESS_MODE = 'w' #rewrite




# open() function

with RESOURCE:
    # pocessing

    pass
'''

import pathlib


PROJECT_ROOT = pathlib.Path(__file__).parent
NEW_FILE_PATH = PROJECT_ROOT.joinpath("text1.txt")
ACCESS_MODE = 'r' # Append
'''
Character	Meaning
'r'	        open for reading (default)
'w'	        open for writing, truncating the file first
'x'	        create a new file and open it for writing
'a'	        open for writing, appending to the end of the file if it exists
'b'	        binary mode
't'	        text mode (default)
'+'	        open a disk file for updating (reading and writing)
'''
# open() function
'''
with RESOURCE:
    # pocessing

    pass
'''

with open(NEW_FILE_PATH, ACCESS_MODE) as f: # f - file object
    file_next_row = f.read() # -> str
    pass

print(file_next_row)

