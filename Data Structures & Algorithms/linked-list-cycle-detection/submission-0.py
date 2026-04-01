# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        track={}

        while head:

            if head in track:
                return True
            
            else:
                track[head]=1
            
            head=head.next
        
        return False

