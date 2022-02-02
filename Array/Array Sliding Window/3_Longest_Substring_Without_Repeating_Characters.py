def lengthOfLongestSubstring(s):
    visited = set()
    maxLen = 0
    left = 0

    for right in range(len(s)):
        # if char is in visited
        while s[right] in visited:
            # remove the char from the left of the window
            visited.remove(s[left])
            left += 1

        # if char has not been visited
        visited.add(s[right])
        maxLen = max(maxLen, right-left+1) # update maxLen

    return maxLen