class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            Time: O(2^n) because at every node we have 2 options to take or not take an element
            Space: O(n^2) because at most we will have n stack frames and for each stack frame we are storing current list 
        """
        result = []
        
        def backtrack(i, current):
            if i == len(nums):
                result.append(current)
                return
            else:
                backtrack(i+1, current)
                backtrack(i+1, current + [nums[i]])
                
        backtrack(0, [])
        return result

    def subsetsOptimal(self, nums: List[int]) -> List[List[int]]:
        """
            Optimization: instead of creating a copy of current at every node we can recreate the state of the list by popping the last element when backtracking
        
            Time: O(2^n)
            Space: O(n)
        """
        result = []
        
        def backtrack(i, current):
            if i == len(nums):
                result.append(current[:])
                return
            else:
                backtrack(i+1, current)
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
                
        backtrack(0, [])
        return result