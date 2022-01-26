def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # edge cases
    if len(nums) <= 1:
        return
    
    left = 0 # left pointer
    for right in range(len(nums)): # right pointer
        if nums[right] != 0: # if the value is not 0
            nums[left], nums[right] = nums[right], nums[left] # swap the values
            left += 1 # increment the left pointer
