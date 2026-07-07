from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 前序遍历（根→左→右）
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def preorder(node):
            if node is None:
                return
            result.append(node.val)   # 访问根
            preorder(node.left)       # 左子树
            preorder(node.right)      # 右子树
        
        preorder(root)
        return result
    
    # 中序遍历（左→根→右）
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)        # 左子树
            result.append(node.val)   # 访问根
            inorder(node.right)       # 右子树
        
        inorder(root)
        return result
    
    # 后序遍历（左→右→根）
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def postorder(node):
            if node is None:
                return
            postorder(node.left)      # 左子树
            postorder(node.right)     # 右子树
            result.append(node.val)   # 访问根
        
        postorder(root)
        return result


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 构建二叉树
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = Solution()
    print("前序遍历:", s.preorderTraversal(root))   # [1, 2, 4, 5, 3]
    print("中序遍历:", s.inorderTraversal(root))    # [4, 2, 5, 1, 3]
    print("后序遍历:", s.postorderTraversal(root))  # [4, 5, 2, 3, 1]