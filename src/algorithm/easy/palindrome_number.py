# Description ===> https://leetcode.com/problems/palindrome-number/description/


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False

        first_x = x
        result = x % 10
        x //= 10
        while x // 10 != 0:
            result = (result * 10) + (x % 10)
            x //= 10

        if x != 0:
            result = (result * 10) + (x % 10)
        return first_x == result
