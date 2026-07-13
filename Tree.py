class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def Traversal(self,root):
        result = []
        def mid(root):
            if root == None:
                return
            mid(root.left)
            result.append(root.val)
            mid(root.right)
        mid(root)
        return result
    
    def MaxDepth(self,root):
        self.maxdepth = 0
        def findmax(root,depth):
            if root == None:
                return
            self.maxdepth = max(depth,self.maxdepth)
            findmax(root.left,depth+1)
            findmax(root.right,depth+1)
        findmax(root,0)
        return self.maxdepth
    
    def Reverse(self,root):
        if root == None:
            return
        root.left,root.right = root.right,root.left
        self.Reverse(root.left)
        self.Reverse(root.right)
        return root
        
    def IsSymmetry(self,root):
        if root == None:
            return True
        def Symmetry(left,right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            outside = Symmetry(left.left,right.right)
            inside = Symmetry(left.right,right.left)
            return outside and inside
        return Symmetry(root.left,root.right)
            
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution()
print("中序遍历的值为:",s.Traversal(root))
print("二叉树的深度为:",s.MaxDepth(root))
print("二叉树是不是对称二叉树:",s.IsSymmetry(root))