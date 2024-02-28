import unittest

from src.algorithm.easy.remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicates(unittest.TestCase):

    def test_case_one(self):
        nums = [1, 1, 2]
        k, res = Solution().removeDuplicates(nums)
        assert k == 2
        assert res == [1, 2, 2]

    def test_case_two(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k, res = Solution().removeDuplicates(nums)
        assert k == 5
        assert res == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
