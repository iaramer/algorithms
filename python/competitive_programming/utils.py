# Print 2d array pretty
def printmx(arr):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in arr]))
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
# [[1, 2, 3], [4, 5, 6]]
printmx(matrix)
# 1 2 3
# 4 5 6

# Count occurrences / find N most common
from collections import Counter
arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
counter = Counter(arr)
top_three = counter.most_common(3)
print(top_three)
# [(1, 5), (3, 4), (4, 3)]
# Counter('abracadabra').most_common(3) -> [('a', 5), ('b', 2), ('r', 2)]
dict(counter.most_common(3))  # to dict

# The n-largest/n-smallest function using heapq
import heapq
grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print(heapq.nlargest(3, grades))  # desc
# [110, 95, 90]
print(heapq.nsmallest(4, grades))  # asc
# [20, 25, 33, 38]

# Sort dict using zip
stocks = {'Goog': 520.54, 'FB': 76.45, 'yhoo': 39.28, 'AMZN': 306.21, 'APPL': 99.76}
zipped_1 = sorted(zip(stocks.values(), stocks.keys()))  # sorting according to values
print(zipped_1)  # [(39.28, 'yhoo'), (76.45, 'FB'), (99.76, 'APPL'), (306.21, 'AMZN'), (520.54, 'Goog')]
zipped_2 = sorted(zip(stocks.keys(), stocks.values()))  # sorting according to keys
print(zipped_2)  # [('AMZN', 306.21), ('APPL', 99.76), ('FB', 76.45), ('Goog', 520.54), ('yhoo', 39.28)]

# Permutations and combinations
from itertools import permutations
perm = list(permutations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
from itertools import combinations
comb = list(combinations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 3)]
