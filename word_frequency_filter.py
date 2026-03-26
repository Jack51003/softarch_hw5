import sys

# get N from the command line argument
n_min = int(sys.argv[1]) if len(sys.argv) > 1 else 1
counts = {}

# collect all words first to count them accurately
for line in sys.stdin:
    word = line.strip()
    if word:
        counts[word] = counts.get(word, 0) + 1

# output words that meet the threshold
for word, count in counts.items():
    if count >= n_min:
        print(word)