class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_tail(head, val):
            new_node = ListNode(val)
            # 如果链表为空
            if not head:
                return new_node
            # 找到最后一个节点
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            return head
        jinwei = ListNode()
        l3 = ListNode()
        # 当l1或者l2存在时   
        while l1 or l2: 
            # 如果l1与l2为None或者不存在时，此时就新建ListNode(0)，将l1或l2赋值0
            if l1 == None or not l1: 
                l1 = ListNode()
            if l2 == None or not l2:
                l2 = ListNode()
            # 3个ListNode进行相加，如果大于10则需要进位。1赋给jinwei，进位余数付给l3，所以需要 l3_val -= 10
            l3_val = l1.val + l2.val + jinwei.val
            if l3_val >= 10:
                l3_val -= 10
                jinwei = add_tail(jinwei, 1)
            else:
                jinwei = add_tail(jinwei, 0)
            # l3 进行尾添加
            l3 = add_tail(l3, l3_val)
            # 重新定义head
            l1 = l1.next
            l2 = l2.next
            jinwei = jinwei.next
        # 如果最后jinwei还有一个值且等于1，则将其尾添加给l3
        if jinwei.val == 1:
            l3 = add_tail(l3, jinwei.val)
        l3 = l3.next
        return l3


  
    
l1_0 = ListNode(9)
l1_1 = ListNode(9)
l1_2 = ListNode(9)
l1_3 = ListNode(9)
l1_4 = ListNode(9)
l1_5 = ListNode(9)

l2_0 = ListNode(9)
l2_1 = ListNode(9)
l2_2 = ListNode(9)

l1_0.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = None

l2_0.next = l2_1
l2_1.next = l2_2
l2_2.next = None

def traverse(head):
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print('None')

traverse(l1_0)
traverse(l2_0)

a = Solution().addTwoNumbers(l1_0, l2_0)
traverse(a)
