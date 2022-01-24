def sortedSquares(nums):
    """
    Initial Approach: (final solution)
        - Iterate over the part of the array that needs to be rotated (n-k to n) and add it to result array
        - Iterate over the rest of the array (0 to k) and add it to result array
        - Return result array

    Analysis:
        - Time: O(n) becasue we have to iterate over every element in the array
        - Space: O(n) because we have to create a new array (result) of the same size
    """
    
    # Two pointers
    left = 0
    right = len(nums)-1

    # Initialize result array
    result = []
    
    # While left less than or eual to the right pointers
    while left <= right:
        # If value of the left pointer is greater than right pointer
        if abs(nums[left]) > abs(nums[right]):
            # Add the square of the left pointer to the result array
            result.insert(0, nums[left]**2)
            left += 1 # Increment left pointer
        else:
            # Add the square of the right pointer to the result array
            result.insert(0, nums[right]**2)
            right -= 1
        
    return result



# does not work for all negative numbers in a list
def sortedSquaresSolution2(nums):
    """
    Initial Approach: (failed solution)
        - Create a left=0 and right=n-1 pointer
        - Compare the values of the left and right pointers
        - Only move the right pointer, all the elements to the right of the right pointer are squared

    Analysis:
        - Time: O(n) becasue we have to iterate over every element in the array
        - Space: O(1) because we are doing it in place
    """
    # initilize the 2 pointers
    left = 0
    right = len(nums)-1
    
    while left < right:
        # compare the elements
        if nums[left]**2 > nums[right]**2:
            swapSquared(nums, left, right)
        elif nums[left]**2 == nums[right]**2:
            squareRight(nums, right)
            swapSquared(nums, left, right)
        else:
            squareRight(nums, right)
            squareRight(nums, right)
            
    return nums

def squareRight(nums, right):
    nums[right] = nums[right]**2
    right -= 1
def swapSquared(nums, left, right):
    nums[left], nums[right] = nums[right], nums[left]
    nums[right] = nums[right]**2
    right -= 1