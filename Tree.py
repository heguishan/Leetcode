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
    
    def Diameter(self, root):
        self.length = 0
        def diameter(root):
            if root == None:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.length = max(left+right,self.length)
            return max(left,right)
        diameter(root)
        return self.length

    def LevelOrder(self,root):
        result = []
        def levelorder(root,depth):
            if root == None:
                return
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            levelorder(root.left,depth+1)
            levelorder(root.right,depth+1)
        levelorder(root,0)
        return result 

    def SortedArray(self,nums):
        def sortedarray(left,right):
            if left > right:
                return
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = sortedarray(left,mid-1)
            root.right = sortedarray(mid+1,right)
            return root
        return sortedarray(0,len(nums)-1)
    
    def IsValidBST(self,root):
        def isvalidBST(root,left,right):
            if root == None:
                return True
            if root.val <= left or root.val >= right:
                return False
            return isvalidBST(root.left,left,root.right.val) and\
            isvalidBST(root.right,root.val,right)
        return isvalidBST(root,float('-inf'),float('inf'))
    
    def topk(self,root):
        Traversal = []
        def Topk(root,k):
            if root == None:
                return None
            Topk(root.left,k)
            Traversal.append(root.val)
            if len(Traversal) == k:
                return toot.val
            Topk(root.right,k)
        Traversal(root,k)
        return Traversal[k-1]

    def rightSideView(self,root):
        result = []
        def RSV(root,depth):
            if root == None:
                return
            if len(result) == depth:
                result.append(root.val)
            RSV(root.right,depth+1)
            RSV(root.left,depth+1)
        RSV(root,0)
        return result

            
            

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
nums = [1,2,3,4,5]
s = Solution()
print("中序遍历的值为:",s.Traversal(root))
print("二叉树的深度为:",s.MaxDepth(root))
print("二叉树是不是对称二叉树:",s.IsSymmetry(root))
print("二叉树右视图为：",s.rightSideView(root))