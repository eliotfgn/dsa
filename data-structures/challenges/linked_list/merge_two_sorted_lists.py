from linked_list import ListNode

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head: ListNode = list1
        prev: ListNode = None
        while list2:
            while list1 and list2 and list2.val >= list1.val:
                print("iterate")
                prev = list1
                list1 = list1.next
                list2 = list2.next

            if list1 and list1.val == head.val:
                list2.next = list1
                head = list2
                prev = head
            else:
                prev.next = list2
                _next1 = list1.next
                _next2 = list2.next
                list2.next = list1
                list2 = _next2
                prev = list1

            list1 = list1.next

        return head


sol = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

res = sol.mergeTwoLists(l1, l2)

while res:
    print(res.val, end="->")
