def sortedSquares(nums):
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