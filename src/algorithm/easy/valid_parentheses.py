# Description ===> https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        is_valid = False
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif char in {')', '}', ']'}:
                if not len(stack):
                    is_valid = False
                    break
                last_val = stack.pop()
                if last_val == '(' and char == ')':
                    is_valid = True
                elif last_val == '{' and char == '}':
                    is_valid = True
                elif last_val == '[' and char == ']':
                    is_valid = True
                else:
                    is_valid = False
                    break

        return False if len(stack) else is_valid




# from collections import deque
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) == 1:
#             return False
#         stack = deque()
#         is_valid = False
#         for char in s:
#             if char in {'(', '{', '['}:
#                 stack.append(char)
#             elif char in {')', '}', ']'}:
#                 if not len(stack):
#                     is_valid = False
#                     break
#                 last_val = stack.pop()
#                 if last_val == '(' and char == ')':
#                     is_valid = True
#                 elif last_val == '{' and char == '}':
#                     is_valid = True
#                 elif last_val == '[' and char == ']':
#                     is_valid = True
#                 else:
#                     is_valid = False
#                     break
#
#         return False if len(stack) else is_valid