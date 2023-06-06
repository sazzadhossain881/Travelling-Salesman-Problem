
n = 10  # there are ten nodes in graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using
# all-pair shortest path algorithms
dist = [
    [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875,100],
    [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589,200],
    [1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940,300],
    [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466,400],
    [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796,500],
    [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547,600],
    [959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891,700],
    [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038,800],
    [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744,900],
    [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0,100],
    [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679,200],
    [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272,300],
    [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162,400],
]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
    # base case
    # if only ith bit and 1st bit is set in our mask,
    # it implies we have visited all other nodes already
    if mask == ((1 << i) | 3):
        return dist[1][i]

    # memoization
    if memo[i][mask] != -1:
        return memo[i][mask]

    res = 10**9  # result of this sub-problem

    # we have to travel all nodes j in mask and end the path at ith node
    # so for every node j in mask, recursively calculate cost of
    # travelling all nodes in mask
    # except i and then travel back from node j to node i taking
    # the shortest path take the minimum of all possible j nodes
    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res  # storing the minimum value
    return res


# Driver program to test above logic
ans = 10**9
for i in range(1, n+1):
    # try to go from node 1 visiting all nodes in between to i
    # then return from i taking the shortest route to 1
    ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

print("The cost of most efficient ride = " + str(ans))