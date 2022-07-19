import sys
N = int(sys.stdin.readline())
for _ in range(N):
    sentence = sys.stdin.readline().split()
    for words in sentence:
        words = words[::-1]
        print(words + " ", end="")
    print("")    