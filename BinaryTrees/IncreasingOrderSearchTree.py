class TreeNode:
    def __init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def increasingBST(self, root):
        # here dummy and tail point to same memory location, will want to return dummy.right 
        # as dummy.right will always point to the beginning of the 
        dummy = TreeNode()
        tail = dummy

        while node is not None:
            if node.left is not None:
                predecessor = node.left 
                while predecessor.right is not None:
                    predecessor = predecessor.right
                predecessor.right = node
                left, node.left = node.left, None
                node = left
            # so this is when the tail is able to find the node for the dummy to "attach" to, essentially
            # the dummy and tail both point to a random TreeNode() in memory, but as we make our 
            # way down to tree to find the first node in the inorder traversal, dummy and tail are still set
            # to the random tree node, so then after we reach a point to where we don't have a left subtree,
            # we set the dummy to this node, thus below, when we do tail.right = node,
            # in memory, tail and dummy are still the same, so the random node they both referencing to, the right 
            # child of that random node now points to first item in the tree, so then when we do tail = node,
            # the tail is no longer pointing to that random node, it is now pointing to the node we just set
            # as the right child 
            else:
                tail.right = node
                tail = node
                node = node.right

        return dummy.right


# so in summary, by doing this, we essentially create links between predecessors 
# and thus can traverse the tree
# 1) so essentially if tree has left subtree, and we start at root, want to find the predecessor, which would be 
# the rightmost element in the left subtree, because if you think about inorder traversal, 
# (say we start at the root), well after traversing the left subtree, when do we eventually get back
# to the root? we would get back after hitting the rightmost node in the subtree because of 
# left -> visit -> right 
# 2) we need to find the first node in this 
# tree, to do so, we must get a point where the node has no more left subtrees, because 
# of left -> visit -> right, thus if no longer have a left, we must visit, thus in the above algorithm
# when we hit the else, the first time, this will set the dummy to the first node in the new tree
# 3) i think that the point of the if statements is to create new links from predecessor to successor, 
# 4) i think else statement is also for when we are stuck ina 