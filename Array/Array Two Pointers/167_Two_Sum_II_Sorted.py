def twoSum(numbers, target):
    """
        Optimal Approach: 
            - key word: sorted array, which means we can use two pointer apprach
            - left pointer starts at 0 and right pointer starts at n
            - move the pointers until the target is found

            Analysis:
                - Time: O(n) becasue we have to iterate over the elements once 
                - Space: O(1)
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        currSum = numbers[left] + numbers[right]
        
        if currSum > target:
            # decrese the sum
            right -= 1
        elif currSum < target:
            # increase the sum
            left += 1
        else:
            return [left+1, right+1]


"""
    Optimal Approach 1: 
        - have a hashmap key=target-number, value=index
        - if an element is in the hashmap, return the index of the element and the index of the element in the array

        Analysis:
            - Time: O(n) becasue we have to iterate over the elements once and check the hashmap
            - Space: O(n) because we are using a hashmap
    

    Initial Approach: 
        - have a nested for loop
        - find 2 numbers in the array that add up to the target

        Analysis:
            - Time: O(n^2) becasue we have to iterate over n elements for each element in the array
            - Space: O(1) because we are not initializing any new auxiliary data structures
"""