class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # result = []
        
        # def climbStairs(n, curCost):
        #     if n <= 1:
        #         result.append(curCost)
        #     else:
        #         climbStairs(n-1, curCost+cost[n-1])
        #         climbStairs(n-2, curCost+cost[n-2])
                
        # climbStairs(len(cost), 0)
        # return min(result)

        def climbStairs(n, curCost):
            if n <= 1:
                return curCost
            else:
                return min(climbStairs(n-1, curCost+cost[n-1]), climbStairs(n-2, curCost+cost[n-2]))
                
        temp = climbStairs(len(cost), 0)
        return temp

