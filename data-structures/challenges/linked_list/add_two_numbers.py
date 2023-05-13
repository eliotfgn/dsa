from linked_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        head = res
        first = True
        r = 0

        while l1 and l2 and r != 0:
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val

            c = a + b
            if c >= 10:
                c = c - 10
                r = 1
            else:
                r = 0
            res.val += c
            res.next = ListNode(r)
            if first:
                head = res
                first = False
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return head


sol = Solution()
i = sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
while i:
    print(i.val)
