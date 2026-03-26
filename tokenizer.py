import sys
import re

for line in sys.stdin:
    # Use regex to find words (ignoring punctuation)
    words = re.findall(r'\b\w+\b', line)
    for word in words:
        print(word)