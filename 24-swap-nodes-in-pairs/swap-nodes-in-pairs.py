class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Swapping nodes
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev two nodes forward
            prev = first
        
        return dummy.next