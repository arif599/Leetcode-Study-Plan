# link: https://leetcode.com/problems/first-bad-version/

def firstBadVersion(n):
    low = 1 # Low index
    high = n # High index
    result = -1 # Result index

    while low <= high: # While low index is less than or equal to high index
        mid = low + ( high - low ) // 2 # Find mid, since low starts at 1, we need to add low to mid to get the actual index

        if isBadVersion(mid): # search left half
            high = mid - 1
            result = mid
        else: # search right half
            low = mid + 1
        
    return result