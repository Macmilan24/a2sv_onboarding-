# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
books =list(map(int, input().split()))
book_count = 0
time_used = 0
left = 0


for right in range(n):
    
    time_used += books[right]
    
    while time_used > t:
        time_used -= books[left]
        left += 1
    
    window = right - left + 1
    book_count = max(book_count, window)
    

print(book_count)