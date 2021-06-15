from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        lists = list()
        lists.append([1])
        if num_rows == 1:
            return lists

        lists.append([1, 1])
        for i in range(2, num_rows):
            prev = lists[-1]
            temp = [None] * (i + 1)
            temp[0] = 1
            temp[-1] = 1
            i, j = 0, 1
            while j < len(prev):
                temp[j] = prev[i] + prev[j]
                i += 1
                j += 1

            lists.append(temp)
        return lists


