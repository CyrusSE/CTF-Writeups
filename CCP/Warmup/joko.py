def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def findgcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
        if result == 1:  
            break
    return result

def solve(N, M, A, que):
    numbers = A.copy() 
    result = []
    for idx, x in que:
        numbers[idx-1] //= x
        gcd = findgcd(numbers)
        result.append(gcd)
    
    return result

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    que = []
    for _ in range(M):
        idx, x = map(int, input().split())
        que.append((idx, x))
    result = solve(N, M, A, que)
    for res in result:
        print(res)

if __name__ == "__main__":
    main()