from collections import Counter

cost = 0

def solution(coupons):
    total_costs = []

    for i in range(len(coupons)):
        coupon = coupons[i]
        cost = returnCost(coupons,coupon)
        total_costs.append(cost)

    return min(total_costs)

def returnCost(coupons,coupon):
    for coupon in coupons:
        if coupon not in coupons:
            cost = -1
            return cost
        else:
            if coupon not in

    return cost

coupons = [5,3,4,2,3,4,5,7]
solution(coupons)
