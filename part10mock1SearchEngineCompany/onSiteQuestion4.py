def solution(num):

    if num < 0:
        return ValueError

    if num == 1:
        return 1

    for k in range((num/2)+1):

        if k**2 == num:
            return k
        elif k**2 > num:
            return k - 1

    return k


print(solution(14))










