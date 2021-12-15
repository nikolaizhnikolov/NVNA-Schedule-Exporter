import hashlib
import os
 
# Get cwd and all script file names, plus the expected .exe in the build folder
# If a file is missing or the structure does not match, this script will throw an error
CWD = os.path.dirname(__file__)
PARENT_CWD = os.path.dirname(CWD) 
files = [
    CWD + '\ExporterInterface.py',
    CWD + '\ExporterRequestProcess.py',
    CWD + '\ExcelExporter.py',
    CWD + '\ExporterInterface.py',
    CWD + '\ExporterLogger.py',
    CWD + '\ExporterHashChecker.py',
    PARENT_CWD + r'\build\dist\NvnaScheduleExporter.exe'
]

# Set hash algorithm
hash = hashlib.sha256()

checksum_file = open('checksums.txt', 'w', encoding='UTF-8')

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
