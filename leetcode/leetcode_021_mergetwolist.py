class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def add_tail(list, val):
            if not list:
                return ListNode(val)
            cur = list
            while cur.next:
                cur = list.next
            cur.next = ListNode(val)
            return list
                
        cur = list1
        while list2:
            base = 0 if not list1 else list1.next.val
            if list2.val <= base:
                list1.next = ListNode(list2.val, list1.next)
                list2 = list2.next
                list1 = list1.next
            # elif base == 0:
            #     list1.next = ListNode(list2.val)
            #     list2 = list2.next
            #     list1 = list1.next
            else:
                list1 = list1.next

        return cur
        
list1_0 = ListNode(1)
list1_1 = ListNode(2)
list1_2 = ListNode(4)

list2_0 = ListNode(1)
list2_1 = ListNode(3)
list2_2 = ListNode(5)

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