def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = 0
    
    for num in arr:
        total += 1
        if num == 0:
            zero += 1
        elif num > 0:
            pos += 1
        else:
            neg += 1
    
    pos_ratio = pos / total
    neg_ratio = neg / total
    zero_ratio = zero / total
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
