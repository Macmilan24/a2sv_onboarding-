# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    i = len(arr) - 1
    
    while arr[i - 1] == arr[i]:
        i -= 1
    
    print(arr[i - 1])