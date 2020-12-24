def remove_duplicates(string):

    result = []
    seen = set()

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)


print(remove_duplicates("tree some"))
