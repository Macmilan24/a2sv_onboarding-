# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    digits = []
    letters = []
    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            letters.append(c)
    
    digits_sorted = sorted(digits)
    letters_sorted = sorted(letters)
    
    is_valid = True
    if digits and letters:
        last_digit_idx = s.rfind(max(digits))
        first_letter_idx = s.find(min(letters))
        if last_digit_idx > first_letter_idx:
            is_valid = False
    
    if digits != digits_sorted or letters != letters_sorted:
        is_valid = False
    
    print("YES" if is_valid else "NO")