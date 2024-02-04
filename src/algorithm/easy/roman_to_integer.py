# Description ===> https://leetcode.com/problems/roman-to-integer/description/


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        skip_index = None
        for i, char in enumerate(s):
            if skip_index and skip_index == i:
                continue
            if i == len(s) - 1 or roman_dict_values[char] >= roman_dict_values[s[i + 1]]:
                result += roman_dict_values[char]
            else:
                result += roman_dict_values[s[i + 1]] - roman_dict_values[s[i]]
                skip_index = i + 1
        return result
