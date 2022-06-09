class Solution:
    def climbStairs(self, n: int) -> int:
        def memoClimbStairs(n, cache={}):
            if n in cache:
                return cache[n]
            if n <= 1:
                cache[n] = 1
            else:
                cache[n] = memoClimbStairs(n-1, cache) + memoClimbStairs(n-2, cache)
            return cache[n]
        return memoClimbStairs(n)

# Time complexity: O(n)
# Space complexity: O(n)