from linked_list import ListNode


class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        # first we should find the last element of the list
        # then we create a new list
        
        reverse: ListNode = None
        prev: ListNode or None = None
        
        while head:
            newNode = ListNode(head.val, prev)
            reverse = newNode
            prev = reverse
            
            head = head.next
        
        return reverse
    
    
    def reverseListOptimized(self, head: ListNode) -> ListNode:
        prev = None
        curr = None

        while head:
            curr = head
            old_next = head.next

            head.next = prev
            prev = head
            
            head = old_next
        
        return curr

    

if __name__ == '__main__':
    sol: Solution = Solution()
    reverse = sol.reverseListOptimized(ListNode(1, ListNode(2, ListNode(3))))
    while reverse:
        print(reverse.val)
        reverse = reverse.next
