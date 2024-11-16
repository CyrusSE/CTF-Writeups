def solve(N):
    digits = list(str(N))
    sorted_digits = sorted(digits, reverse=True) 
    smallest_even = None
    for d in sorted_digits:
        if int(d) % 2 == 0:
            smallest_even = d
    if smallest_even is None:
        return "Mustahil! o_o"
    result = sorted_digits[:]
    result.remove(smallest_even)
    result.append(smallest_even)
    return "".join(result)

def main():
    N = int(input())
    result = solve(N)
    print(result)

if __name__ == "__main__":
    main()