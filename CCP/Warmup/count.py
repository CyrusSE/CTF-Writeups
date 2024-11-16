from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    positions = defaultdict(list)
    for i, num in enumerate(a):
        positions[num].append(i)
    for i in range(n):
        num = a[i]
        for multiple in range(num, 10001, num):
            for pos in positions[multiple]:
                if pos > i: 
                    count += 1
    return count

print(solve())