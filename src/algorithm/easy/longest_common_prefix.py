# Description ===> https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        min_length = min(len(i) for i in strs)
        first = strs[0]
        max_length = 0
        is_equal = True
        for i in range(min_length):
            for str in strs:
                if first[i] != str[i]:
                    is_equal = False
            if is_equal:
                max_length += 1
            else:
                break
        return first[:max_length]
