import sys

# get MIN and MAX from command line arguments
min_len = int(sys.argv[1])
max_len = int(sys.argv[2])

for line in sys.stdin:
    word = line.strip()
    if min_len <= len(word) <= max_len:
        print(word)