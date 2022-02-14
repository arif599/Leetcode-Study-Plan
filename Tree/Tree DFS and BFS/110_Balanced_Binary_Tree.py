class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
            Approach:
                - DFS
                - check if difference in height of left subtree and right subtree is less than or equal to 1
            Analysis:
                - Time: O(n) becasue we have to visit each node
                - Space: O(n) becasue the nodes are stored in a stack
        """
        balanced = True
        def findHeight(node):
            if node == None: # base case
                return 0
            else: # recursive case
                left = findHeight(node.left)
                right = findHeight(node.right)
                if abs(left-right) > 1:
                    nonlocal balanced
                    balanced = False
                return max(left, right)+1
        findHeight(root)
        return balanced