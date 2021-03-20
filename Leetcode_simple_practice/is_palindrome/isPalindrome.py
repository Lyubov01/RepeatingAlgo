def is_palindrome(x):
    """
    Difficulty:easy
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123
    is not.
    """
    s = str(x)
    n = len(s)
    if n % 2 == 0:
        left = s[:n // 2]
        right = s[n // 2:]
    else:
        left = s[:n // 2]
        right = s[n // 2 + 1:]
    k = len(right) - 1
    i = 0
    while i < len(left) and k > -1:
        if left[i] == right[k]:
            i += 1
            k -= 1
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome(43567))
