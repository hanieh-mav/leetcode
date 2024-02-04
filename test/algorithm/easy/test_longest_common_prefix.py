import unittest

from src.algorithm.easy.longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test_case_one(self):
        strs = ["flower", "flow", "flight"]
        res = Solution().longestCommonPrefix(strs)
        assert res == 'fl'

    def test_case_two(self):
        strs = ["dog", "racecar", "car"]
        res = Solution().longestCommonPrefix(strs)
        assert res == ''


if __name__ == '__main__':
    unittest.main()
