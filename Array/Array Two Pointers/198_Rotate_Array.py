def rotate(nums, k):
    # Time: O(n) becasue we have to iterate over every element in the array
    # Space: O(n) because we have to create a new array (result) of the same size
    
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