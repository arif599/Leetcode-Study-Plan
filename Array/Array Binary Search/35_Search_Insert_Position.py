# link: https://leetcode.com/problems/search-insert-position
def searchInsert(nums, target):
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] > target:
            # search left half
            high = mid - 1
        elif nums[mid] < target:
            # search right half
            low = mid + 1
        else:
            return mid # if the target is found in the array then return that index
    
    return low # this is where the target should have been