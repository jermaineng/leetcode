# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # stack containing smallest element at top
        def push_left(st, root):
            while root:
                st.append(root)
                root = root.left
        
        # stack containing largest element at top
        def push_right(st, root):
            while root:
                st.append(root)
                root = root.right
        
        # returns next smallest element
        def next_left(st):
            node = st.pop()
            push_left(st, node.right)
            return node.val

        # returns next largest element
        def next_right(st):
            node = st.pop()
            push_right(st, node.left)
            return node.val
        
        left_st, right_st = [], []
        push_left(left_st, root)
        push_right(right_st, root)

        left = next_left(left_st)
        right = next_right(right_st)

        while left < right:
            sum = left + right

            if sum == k:
                return True
            if sum < k:
                left = next_left(left_st)
            else:
                right = next_right(right_st)
            
        return False
