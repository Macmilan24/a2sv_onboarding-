# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

t = int(input())

for _ in range(t):
    
    string = list(input().strip())
    input_count = int(input())
    length = len(string)
    
    count = 0
    
    for j in range(length - 3):
        if string[j] == "1" and string[j + 1] == "1" and string[j + 2] == "0" and string[j + 3] == "0":
            count += 1
            
    
    for j in range(input_count):
        
        i, q = input().split()
        
        i = int(i) - 1
        
        if string[i] == q:
            print("YES" if count > 0 else "NO")
            continue
        
        for j in range(max(0, i - 3), min(i + 1, length - 3)):
            if string[j] == "1" and string[j + 1] == "1" and string[j + 2] == "0" and string[j + 3] == "0":
                count -= 1
        
        string[i] = q
        
        for j in range(max(0, i - 3), min(i + 1, length - 3)):
            if string[j] == "1" and string[j + 1] == "1" and string[j + 2] == "0" and string[j + 3] == "0":
                count += 1
        
        print("YES" if count > 0 else "NO")        
                