"""
Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:
Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here      '

both become:
'here space'

"""


def rev_word1(s):
    return " ".join(reversed(s.split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])




























