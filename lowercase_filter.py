import sys

for line in sys.stdin:
    word = line.strip()
    if word:
        print(word.lower())