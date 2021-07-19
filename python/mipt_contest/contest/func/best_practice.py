# Get dictionary
dictionary = {'a': 1, 'b': 2}
# print(dictionary['c'])  # Exception
print(dictionary.get('c'))  # None
print(dictionary.get('c', 0))  # Default value is 0

# Ternary / Elvis
x1 = 'true' if True else 'false'  # Standard
x2 = ('false', 'true')[2>1]  # Advanced (falseValue, trueValue)[bool(<expression>)]

# Remove duplicates
some_list = [1, 2, 3, 4, 5, 1, 2, 3]
list(set(some_list))  # [1, 2, 3, 4, 5]

# String join
arr = [1, 2, 3]
s1 = ' '.join(map(str, arr))  # Convert list integer to string: '1 2 3'
s2 = '\n'.join(map(str, arr))  # String with line break:
# 1
# 2
# 3

# Tuple to dict with reversed key-values
t = [(1, 'a'), (2, 'b')]
dict((y, x) for x, y in t)
# {'a': 1, 'b': 2}

# String remove spaces and chars
"    \nfd\ts \n   ".strip()  # Removes spaces, line breaks, etc at head and tail of str. Result: 'fd      s'
",,,,,rrttgg.....banana....rrr".strip(",.grt")  # Removes specified chars from head and tail. Result: 'banana'

# Fractions
from fractions import Fraction
Fraction(2.25)  # Fraction(9, 4)
from decimal import Decimal
Fraction(Decimal('1.1'))  # Fraction(11, 10)

# Decimal
from decimal import *
getcontext().prec = 6
Decimal(1) / Decimal(7)  # Decimal('0.142857')
getcontext().prec = 28
Decimal(1) / Decimal(7)  # Decimal('0.1428571428571428571428571429')
