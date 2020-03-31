def maxHorse(horses, budget):
    res = 0
    horses.sort()
    for x in horses:
        if budget - x >= 0:
            budget -= x
            res += 1

    return res


t = int(input())
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    h = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, maxHorse(h, m)))
