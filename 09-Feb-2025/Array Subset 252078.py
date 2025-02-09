# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

n = int(input())  # Read the length of the encoded word
encoded = input().strip()  # Read the encoded string

original = []  # List to store the reconstructed word

# Rebuild the original string by inserting letters at the median position
for ch in reversed(encoded):
    mid = (len(original) + 1) // 2 - 1  # Calculate median position
    original.insert(mid + 1, ch)  # Insert the character at the correct position

print("".join(original))  # Print the reconstructed original word