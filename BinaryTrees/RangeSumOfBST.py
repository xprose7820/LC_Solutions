# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0 
        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    

# so we start of the recursive call with a base case (obviously need to to end the recurise call somehow), 
# then the next lines of code are further processing the inputs, if the val of the current node is greater than the high, 
# this means that any values in the right branch are most likely going to be higher than the "high", vice versa for the low, 
# then if the values are within this range, we simply end the function with a return by grabbing the current nodes values and summing 
# with the subsequent nodes in the call 
        
