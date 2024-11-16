def count_ones(n):
    count = 0
    while n:
        n &= (n - 1) 
        count += 1
    return count

def solve(N, X):
    target_ones = count_ones(X)
    count = 0
    for i in range(1, N + 1):
        if count_ones(i) == target_ones:
            count += 1
            
    return count

def main():
    N, X = map(int, input().split())
    result = solve(N, X)
    print(result)

if __name__ == "__main__":
    main()