from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(nums):
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
class Solution:
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            next_one = curr.next
            curr.next = pre
            pre = curr
            curr = next_one
        return pre

s = Solution()
print(print_linked_list(s.reverseList(create_linked_list([1,2,3,4,5]))))
