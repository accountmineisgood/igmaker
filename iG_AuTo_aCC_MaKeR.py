import sys

# Check version
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
if PYTHON_VERSION != bytes([51, 46, 57]).decode():
    print('''USE OLD PYDRIOD 👽'''.replace("[VERSION]", sys.version.split(" ")[0]))
    exit(0)

import marshal