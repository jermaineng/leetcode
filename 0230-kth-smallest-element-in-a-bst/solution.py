# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            
            curr = curr.right

# inorder traversal of bst gives nodes in sorted order
# use a stack to traverse and end when kth smallest node is reached

# for the follow up qn: use an order statistic tree, i.e. store the size of the subtree in the node
# if the curr node's subtree size is k - 1, the curr node is the kth smallest. if size is smaller, then the kth smallest node is in left subtree. otherwise, right subtree
