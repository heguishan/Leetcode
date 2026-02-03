from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    # 判回文 —— 数组法，不破坏原链表
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals: List[int] = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

# ---------------- 测试 -----------------
if __name__ == "__main__":
    # 构造 1->2->3->2->1
    nodes = [ListNode(i) for i in [1, 2, 3, 2, 1]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    print(Solution().isPalindrome(nodes[0]))  # True