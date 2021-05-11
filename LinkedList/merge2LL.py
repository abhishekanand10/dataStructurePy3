# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         cur1 = l1
#         cur2 = l2
#         cur1s = l1
#
#         if cur1 is None and cur2 is None:
#             return None
#         elif cur1 is None:
#             return cur2
#         elif cur2 is None:
#             return cur1
#
#         if cur1.next is None or cur2.next is None:
#             while cur1.next is not None or cur2.next is not None:
#
#         if cur1.val > cur2.val:
#             cur1 = l2
#             cur2 = l1
#             cur1s = l2
#
#         last = ListNode()
#
#         while cur1.next is not None and cur2.next is not None:
#             if cur1.val <= cur2.val and cur1.next.val >= cur2.val:
#                 temp = cur1.next
#                 cur1.next = cur2
#                 cur2 = cur2.next
#                 cur1 = cur1.next
#                 cur1.next = temp
#
#             last = cur1
#             cur1 = cur1.next
#
#         if cur1.val >= cur2.val:
#             temp = cur1
#             last.next = cur2
#             last = last.next
#             last.next = temp
#             # last = last.next
#
#         else:
#             temp = cur2
#             last.next = cur1
#             last = last.next
#             last.next = temp
#             last = last.next
#
#         return cur1s