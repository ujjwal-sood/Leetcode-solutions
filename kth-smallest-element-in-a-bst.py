# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
    	#MY SOLUTION
        l=[k]
        def ks(r):
            if r==None:
                return
            t1=ks(r.left)
            if t1!=None:
                return t1
            l[0]-=1
            if l[0]==0:
                return r.val
            t2=ks(r.right)
            return t2
        return ks(root)
        # LESS VARIABLE SOL.
    """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)
    """