def solve(N, arr):
    total = 0 
    for i in range(N):
        if arr[i] < 0:
            total += -arr[i]
        else:
            total += arr[i]
    return total

N = int(input())
arr = list(map(int, input().split()))

hasil = solve(N, arr)
print(hasil)