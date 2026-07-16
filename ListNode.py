class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, ListA, ListB):
        if ListA == None or ListB == None:
            return None
        pA = ListA
        pB = ListB
        while pA != pB:
            if pA != None:
                pA = pA.next
            else:
                pA = ListB
            if pB != None:
                pB = pB.next
            else:
                pB = ListA
        return pA

    def reverseList(self, head):
        if head == None:
            return None
        curr = head
        pre = None
        while curr != None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
    
    def Palindrome(self,head):
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow
        pre = None
        while right:
            temp = right.next
            right.next = pre
            pre = right
            right = temp
        while pre:
            if pre.val != left.val:
                return False
            pre = pre.next
            left = left.next
        return True

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr.next = ListNode((val1+val2+carry)%10) #顺序、不能直接赋值
            carry = (val1+val2+carry)//10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

ListA = ListNode(4)
ListA.next = ListNode(1)
ListA.next.next = common

ListB = ListNode(5)
ListB.next = ListNode(6)
ListB.next.next = ListNode(1)
ListB.next.next.next = common

s = Solution()
print("两个链表的起点为",s.getIntersectionNode(ListA,ListB))
print("链表A是否为回文链表", s.Palindrome(ListA))
