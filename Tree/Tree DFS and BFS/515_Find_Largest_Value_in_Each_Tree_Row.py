class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        results = []
        import math
        levelMax = -math.inf

        import collections 
        queue = collections.deque()
        queue.append(root)
        queue.append(None)

        while queue:
            current = queue.popleft()

            if current == None:
                results.append(levelMax)
                levelMax = -math.inf


                if len(queue) != 0:
                    queue.append(None)
            else:
                levelMax = max(levelMax, current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return results
# Time: O(n) because we are iterating over every node in the tree
# Space: O(2n)=O(n) because of the extra space used for results and queue
