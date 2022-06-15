def minCost(cost):
    # cost[i][j] where i = house and j = color

    dp = cost[0]

    for i in range(1, len(cost)):
        dp0 = cost[i][0] + min(dp[1], dp[2])
        dp1 = cost[i][1] + min(dp[0], dp[2])
        dp2 = cost[i][2] + min(dp[0], dp[1])
        dp = [dp0, dp1, dp2]

    return min(dp)

print(minCost([[17,2,17],[16,16,5],[14,3,19]]))