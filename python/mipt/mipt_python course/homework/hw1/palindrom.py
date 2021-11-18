"""
Create a palindrome from given string. For example, "abc" -> "abcba" *
"""


def palindrome(s: str) -> str:
    if not s:
        return ''
    if s == s[::-1]:
        return s
    for i in range(len(s)):
        s1 = s + s[i::-1]
        if s1 == s1[::-1]:
            return s1


if __name__ == '__main__':
    inp = 'abc'
    ans = 'abcba'
    assert palindrome(inp) == ans

    inp = ''
    ans = ''
    assert palindrome(inp) == ans

    inp = 'a'
    ans = 'a'
    assert palindrome(inp) == ans

    inp = 'aba'
    ans = 'aba'
    assert palindrome(inp) == ans

    inp = 'abcc'
    ans = 'abccba'
    assert palindrome(inp) == ans

    inp = 'abcb'
    ans = 'abcba'
    assert palindrome(inp) == ans

    print('OK')
