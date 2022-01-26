def moveZeroes(nums):
    """
    Optimal Approach: 
        - use the two pointer approach
        - left pointer starts at 0
        - right pointer = 0 to n in the for loop
        - if the value of the right pointer is not 0, then swap the values of the left pointer and right pointer
        - increment the left pointer by 1 and the right pointer will automatically increment by 1

    Analysis:
        - Time: O(n) becasue the 2 pointers only iterate over the array once
        - Space: O(1) because we are doing it in place
    """
    # edge cases
    if len(nums) <= 1:
        return
    
    left = 0 # left pointer
    for right in range(len(nums)): # right pointer
        if nums[right] != 0: # if the value is not 0
            nums[left], nums[right] = nums[right], nums[left] # swap the values
            left += 1 # increment the left pointer

"""
Initial Approach: 
    - iterate over the array and add non-zeroes to result array
    - add zeroes to result array (# of zero's = n - len(result))
    - Return result array

Analysis:
    - Time: O(n) becasue we have to iterate over every element in the array
    - Space: O(n) because we have to create a new array (result) of the same size
"""