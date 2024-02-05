# Description ===> https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = [self.val]
        my_next = self.next
        while my_next:
            res.append(my_next.val)
            my_next = my_next.next
        return str(res)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val > list2.val:
            res.val = list2.val
            list2 = list2.next
        else:
            res.val = list1.val
            list1 = list1.next

        current_node = res

        while list1 is not None or list2 is not None:
            if list1 is None:
                current_node.next = list2
                break

            if list2 is None:
                current_node.next = list1
                break


            if list1.val > list2.val:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            current_node = current_node.next

        return res
