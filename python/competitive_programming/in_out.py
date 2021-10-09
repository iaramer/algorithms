"""" stdin """
# Change input from standard input to file:
import sys
sys.stdin = open('in.txt', 'r')
# Change output from standard output to file:
sys.stdout = open('out.txt', 'w')

# Read an integer from standard input:
n = int(input())

# Read an integer array from standard input:
arr = list(map(int, input().split()))

# Read str from std multiline (first param is the number of input rows). Format: [('1','2'),(...),(),(...)]
inp = list()
for i in range(int(input())):
    inp.append(tuple(input().split()))

# Read int from std multiline (first param is the number of input rows). Format: [(1,2),(...),(),(...)]
inp = list()
for i in range(int(input())):
    inp.append(tuple(map(int, input().split())))

""" stdout """
# Change output from standard output to file:
import sys
sys.stdout = open('out.txt', 'w')

# Print array to Standard output
arr = [1, 2, 3]
print(*arr)


