# 1) Calculate the cumulative sum
def rec_sum(n):

    # Base Case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)


# 2) Return the sum of all individual digits in that integer
def sum_func(n):

    # Base Case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n/10)


# 3) A function to create possible
def word_split(phrase, list_of_words, output=None):

    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startsWith(word):
            output.append(word)

            return word_split( phrase[len(word):], list_of_words, output)

    return output







