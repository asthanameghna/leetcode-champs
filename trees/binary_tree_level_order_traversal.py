# # Approach
# Use **Breadth-First Search (BFS)** with a queue to traverse the tree level by level.  
# For each iteration, determine how many nodes belong to the current level (`level_size`).  
# Process exactly those nodes, collect their values, and add their children to the queue for the next level.  
# Append the collected values to the result.

# # Time Complexity
# **O(n)**  
# Each node in the tree is visited exactly once.

# # Space Complexity
# **O(n)**  
# The queue may contain up to all nodes in the largest level of the tree.

########## PSEUDO CODE ###########
# FUNCTION levelOrder(root):

#     IF root is null
#         RETURN empty list

#     result = empty list
#     queue = [root]

#     WHILE queue is not empty

#         level_size = number of nodes currently in queue
#         level = empty list

#         REPEAT level_size times

#             node = remove first element from queue

#             add node.value to level

#             IF node.left exists
#                 add node.left to queue

#             IF node.right exists
#                 add node.right to queue

#         add level to result

#     RETURN result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []    
        queue = [root]

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result  

