def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
    route_sums = []

    for i, n in forwardRouteList:
        for j, k in returnRouteList:
            route_sums.append([[i, j], k + n])

    best_sum = 0

    for route, sum in route_sums:
        if sum <= maxTravelDist:
            best_sum = max(best_sum, sum)

    result = []

    for route, sum in route_sums:
        if sum == best_sum:
            result.append(route)
    return result

print(routePairs(7000,[[1,2000],[2,4000],[3,6000]],[[1,2000]]))