import hashlib
import os
import datetime
 
# Get cwd and all script file names, plus the expected .exe in the build folder
# If a file is missing or the structure does not match, this script will throw an error
CWD = os.path.dirname(__file__)
PARENT_CWD = os.path.dirname(CWD) 

files = [PARENT_CWD + r'\build\dist\NvnaScheduleExporter.exe']

for file in os.listdir(CWD):
    if file.endswith(".py"):
        files.append(os.path.join(CWD, file))

# Set hash algorithm
hash = hashlib.sha256()

# Overwrite file each time
checksum_file = open(os.path.join(CWD, 'checksums.txt'), 'w', encoding='UTF-8')
checksum_file.write("Last update at: " + str(datetime.datetime.now()) + "\n\n")

# For each file
for file in files:
    with open(file, "rb") as f:
        # Read entire file as bytes, shouldn't be a memory issue.
        # Largest file is the .exe, which is about ~12MBs
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        filename = file.split('\\').pop()
        checksum_file.write(filename + ": " + readable_hash+'\n')
        f.close()
checksum_file.close()
