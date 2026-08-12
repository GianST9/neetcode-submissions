# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None   # previous node
        current = head # pointer to the current node

        while current: # while not None
            next_node = current.next # store next node, of the old list
            current.next = prev # reversel: "relink" next node as the previous
            prev = current # current node will be the prev
            current = next_node # finally current node is set to next_node from above

        return prev