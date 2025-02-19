# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

t = int(input())
chat_list = {}

for _ in range(t):
    chat = input().strip()
    
    if chat in chat_list:
        del chat_list[chat]
    chat_list[chat] = None

print("\n".join(reversed(chat_list.keys())))