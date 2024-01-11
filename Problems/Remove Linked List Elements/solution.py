from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy

        while current_node.next:
            if current_node.next.val == val:
                # Remove node
                current_node.next = current_node.next.next
            else:
                # Just advance
                current_node = current_node.next

        return dummy.next
