import unittest

from src.algorithm.easy.remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicates(unittest.TestCase):

    def test_case_one(self):
        nums = [1, 1]
        k = Solution().removeDuplicates(nums)
        assert k == 2

    def test_case_two(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = Solution().removeDuplicates(nums)
        assert k == 5


    def test_case_three(self):
        nums = [0]
        k = Solution().removeDuplicates(nums)
        assert k == 1


    def test_case_four(self):
        nums = []
        k = Solution().removeDuplicates(nums)
        assert k == 0
