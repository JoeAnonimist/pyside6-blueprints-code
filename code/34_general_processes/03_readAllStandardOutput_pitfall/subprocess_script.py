import os
import sys
import time

text = (
    "This is a long demonstration sentence"
    " that will be split into arbitrary chunks"
    " without regard for newlines or word boundaries"
    " if you don't buffer the output." + os.linesep)
full_text = text * 5

for i in range(0, len(full_text), 20):  # 20-byte chunks
    sys.stdout.write(full_text[i:i+20])
    sys.stdout.flush()  # Trigger readyRead
    time.sleep(0.1)