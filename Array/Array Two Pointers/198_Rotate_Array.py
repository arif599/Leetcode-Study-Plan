def rotateSolution2(nums, k):
    """
    Optimal Approach: 
        - Trying to optimize the space complexity by doing it in place
        - Reverse the array using two pointer apprach
        - Then reverse the array form 0 to k-1 
        - Then reverse the array from K to n part of the array

    Analysis:
        - Time: O(n) becasue we have to iterate over every element in the array
        - Space: O(1) because we are doing it in place
    """
    # Base cases
    if len(nums) <= 1:
        return nums
    if k > len(nums):
        k = k%len(nums) # if k is greater than the length of the array then we need to mod k by the length of the array
    
    # reverse the entire array in place
    reserveList(nums, left = 0, right = len(nums)-1) 
    # reverse the array from 0 to k-1
    reserveList(nums, left = 0, right = k-1)
    # reverse the array from K to n
    reserveList(nums, left = k, right = len(nums)-1)

    return nums

def reversePartofList(nums, left, right):
    while left < right:
        # swap the elements
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right += 1

def rotate(nums, k):
    """
    Initial Approach: 
        - Iterate over the part of the array that needs to be rotated (n-k to n) and add it to result array
        - Iterate over the rest of the array (0 to k) and add it to result array
        - Return result array

    Analysis:
        - Time: O(n) becasue we have to iterate over every element in the array
        - Space: O(n) because we have to create a new array (result) of the same size
    """

    
    result = []

    # initialize start to part of the array that needs to be at the front
    start = len(nums)-k
    for i in range(start, len(nums)):
        # iterate over the array from n-k to n and add the values to the result array
        result.append(nums[i])
        
    for i in range(0, k+1):
        # iterate over the array from 0 to k and add the values to the result array
        result.append(nums[i])
        
    return result