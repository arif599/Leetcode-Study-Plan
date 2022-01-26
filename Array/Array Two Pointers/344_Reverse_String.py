def reverseString(s):
    """
        Optimal Approach: 
            - Two pointer apprach
            - left pointer starts at 0 and right pointer starts at n-1
            - swap the values of the left pointer and right pointer
            - increment the left pointer by 1 and decrement the right pointer by 1

            Analysis:
                - Time: O(n) becasue we have to iterate over every element in the array
                - Space: O(1) because we will be doing it in place
    """
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

"""
    Initial Approach: 
        - iterate over the array from the end
        - add elements to the reverse array

        Analysis:
            - Time: O(n) becasue we have to iterate over every element in the array
            - Space: O(n) because we have to store the reverse array
"""