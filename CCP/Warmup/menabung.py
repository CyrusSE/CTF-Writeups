def min_days_to_save(n, X, A):
    if n == 1:
        return (X + A[0] - 1) // A[0]  
    cycle_sum = sum(A)
    full_cycles = X // cycle_sum
    remaining_target = X - (full_cycles * cycle_sum)
    if remaining_target <= 0:
        days = 0
        current_sum = 0
        min_days = float('inf')
        
        for i in range(2 * n): 
            current_sum += A[i % n]
            days += 1
            if current_sum >= X:
                min_days = min(min_days, days)
        return min_days
    days = full_cycles * n
    current_sum = 0
    
    for i in range(2 * n):  
        current_sum += A[i % n]
        if current_sum >= remaining_target:
            return days + i + 1
    return days + n  

def main():
    n, X = map(int, input().split())
    A = list(map(int, input().split()))
    result = min_days_to_save(n, X, A)
    print(result)

if __name__ == "__main__":
    main()