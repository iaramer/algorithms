"""
На вход подаются строки, нужно вернуть список последовательностей скобок
"(1+2)+3=4" -> [(0,4)]
"((1+1)+2)+3=4" -> [(0,8), (1,5)]
"""
from typing import List, Tuple


def func(s: str) -> List[Tuple[int, int]]:
    ans = list()
    stack = list()
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            ans.append((stack.pop(), i))
    return list(reversed(ans))


if __name__ == "__main__":
    inp = '(1+2)+3=4'
    assert func(inp) == [(0, 4)]

    inp = '((1+1)+2)+3=4'
    assert func(inp) == [(0, 8), (1, 5)]
