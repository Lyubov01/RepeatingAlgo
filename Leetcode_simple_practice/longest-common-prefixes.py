from typing import List


def longestCommonPrefix(strs: List[str]):
    shortest = None
    for s in strs:
        if shortest is None or len(shortest) > len(s):
            shortest = s

    prefix = ''

    for i in range(len(shortest)):
        for el in strs:
            if shortest[i] != el[i]:
                return prefix
        prefix += shortest[i]
    return prefix

