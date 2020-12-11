"""
String Compression
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely
"compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this
technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
Solution
Since Python strings are immutable, we'll need to work off of a list of characters, and at the end convert that list
 back into a string with a join statement.
The solution below should yield us with a Time and Space complexity of O(n). Let's take a look with careful attention
to the explanatory comments:
"""


def compression(s):
    """
    This solution compression without checking.
     Known as the RunLength Compression algorithm.
    """
    r = ""
    length = len(s)

    if length == 0:
        return ""

    if length == 1:
        return s + "1"

    last = s[0]
    cnt = 1
    i = 1

    while i < length:

        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i - 1] + str(cnt)

    return r




