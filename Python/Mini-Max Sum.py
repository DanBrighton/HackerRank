def miniMaxSum(arr):
    arr.sort()
    
    low = sum(arr[:4])
    high = sum(arr[1:])
    
    print(f"{low} {high}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
