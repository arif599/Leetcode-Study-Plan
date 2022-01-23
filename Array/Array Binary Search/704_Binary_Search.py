# link: https://leetcode.com/problems/binary-search/

def search(nums, target):
    # time complexity: O(log(n))
    # space complexity: O(1)

    start = 0 # Start index
    end = len(nums) - 1 # End index
    while start <= end: # While start index is less than or equal to end index
        mid = (start + end) // 2 # Find mid
        if nums[mid] == target: # Found
            return mid
        elif nums[mid] < target: # Search right
            start = mid + 1
        else: # Search left
            end = mid - 1
    return -1 # Not found