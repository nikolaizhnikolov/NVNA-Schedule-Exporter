import datetime
import hashlib
import os
import requests
from requests import RequestException

from filecmp import cmp
import ExporterLogger as logger

# Get CWD and all script file names, plus the expected .exe in the build folder
# If a file is missing or the structure does not match, this script will
# throw an error
CWD = os.path.dirname(__file__)
PARENT_CWD = os.path.dirname(CWD)

files = [PARENT_CWD + r'\build\dist\NvnaScheduleExporter.exe']

for file in os.listdir(CWD):
    if file.endswith(".py"):
        files.append(os.path.join(CWD, file))

def hash():
    # Overwrite file each time
    checksum_file = open(os.path.join(CWD, 'checksums.txt'), 'w')
    # checksum_file.write("Last update at: " + str(datetime.datetime.now()) + "\n\n")

    # For each file
    for file in files:
        with open(file, "rb") as f:
        # Read entire file as bytes, shouldn't be a memory issue.
        # Largest file is the .exe, which is about >20MBs
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()
            filename = file.split('\\').pop()
            checksum_file.write(filename + ": " + readable_hash + '\n')
            f.close()
    checksum_file.close()


# Calculate new hashes, then compare against remote repository
def is_tampered():
    try:
        remote_checksums_file = requests.get('https://raw.github.com/nikolaizhnikolov/NVNA-Schedule-Exporter/master/src/checksums.txt')
    except RequestException as e:
        logger.error(e)
        raise SystemExit(e)
    
    hash()
    with open(os.path.join(CWD, 'checksums.txt'), 'r') as local_checksums_file:
        local_checksums_file.seek(0)
        if remote_checksums_file.text is not local_checksums_file.read():
            return True
    return False

    # for file in files:
    #     with open(file, "rb") as f:
    #         readable_hash = hashlib.sha256(f.read()).hexdigest()
    #         if readable_hash not in remote_checksums:
    #             logger.error("Found possible program tampering for: " + file.split('\\').pop())
    #             logger.error("Cannot find hash: " + str(readable_hash))
    #             return True
    # return False
