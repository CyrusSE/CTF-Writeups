def solve(N, K, arr):
    max_val = max(arr)
    total = sum(arr)
    arr.sort()
    for i in range(min(K, N)):
        total += max_val - arr[i]
    return total

N, K = map(int, input().split())
arr = list(map(int, input().split()))

hasil = solve(N, K, arr)
print(hasil)