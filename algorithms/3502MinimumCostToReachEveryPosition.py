def minCosts(cost):


    for i in range(1, len(cost)):
        if cost[i] > cost[i-1]:
            cost[i] = cost[i-1]
    return cost

cost = [5,3,4,1,3,2]
print(minCosts(cost))
