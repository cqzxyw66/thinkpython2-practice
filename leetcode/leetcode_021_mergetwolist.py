class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        
list1_0 = ListNode(1)
list1_1 = ListNode(2)
list1_2 = ListNode(4)

list2_0 = ListNode(1)
list2_1 = ListNode(3)
list2_2 = ListNode(8)

list1_0.next = list1_1
list1_1.next = list1_2
list1_2.next = None

list2_0.next = list2_1
list2_1.next = list2_2
list2_2.next = None

def traverse(head):
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print('None')

b = Solution().mergeTwoLists(list1_0, list2_0)
traverse(b)