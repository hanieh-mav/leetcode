import unittest

from src.algorithm.easy.merge_two_sorted_lists import ListNode, Solution


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_case_one(self):
        list1 = ListNode(1, (ListNode(2, ListNode(4))))
        list2 = ListNode(1, (ListNode(3, ListNode(4))))
        res = Solution().mergeTwoLists(list1, list2)
        assert str(res) == str([1, 1, 2, 3, 4, 4])

    def test_case_two(self):
        res = Solution().mergeTwoLists(None,None)
        assert res is None

    def test_case_three(self):
        res = Solution().mergeTwoLists(None, ListNode())
        assert str(res) == str([0])

if __name__ == '__main__':
    unittest.main()
