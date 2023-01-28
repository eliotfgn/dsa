class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        middle_index = self.lenght(head) // 2
        middle_node = head

        for i in range(0, middle_index):
            middle_node = middle_node.next
        return middle_node


    def lenght(self, list: ListNode) -> int:
        count = 0
        while list:
            count += 1

            list = list.next

        return count

sol = Solution()

print(sol.middleNode(ListNode(0, ListNode(1, ListNode(2, ListNode(1, ListNode(0, ListNode(5))))))).data)