# # Approach
# Use recursion with a valid range for each node.  
# Each node must satisfy:

# min_val < node.val < max_val

# For the left subtree, update the upper bound to the current node value.  
# For the right subtree, update the lower bound to the current node value.  
# If any node violates its allowed range, return `False`.

# # Time Complexity
# **O(n)**  
# Each node is visited once.

# # Space Complexity
# **O(h)**  
# `h` is the height of the tree due to the recursion stack.  
# Worst case: **O(n)**, balanced tree: **O(log n)**

####### Pseudocode — Validate Binary Search Tree #######

# FUNCTION isValidBST(root)

#     FUNCTION validate(node, min_val, max_val)

#         IF node is NULL
#             RETURN True

    #     IF node.value <= min_val OR node.value >= max_val
    #         RETURN False

    #     left_valid  = validate(node.left,  min_val, node.value)
    #     right_valid = validate(node.right, node.value, max_val)

    #     RETURN left_valid AND right_valid

    # RETURN validate(root, -∞, +∞)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_val, max_val):
            if node is None:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False

            left = validate(node.left, min_val, node.val)
            right = validate(node.right, node.val, max_val)

            return (left and right)    
        
        return validate(root, float("-inf"), float("inf"))
        