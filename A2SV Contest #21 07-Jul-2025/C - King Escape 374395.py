# Problem: C - King Escape - https://codeforces.com/gym/619446/problem/C

def solve():
    n = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())

    is_king_x_less = bx < ax
    is_king_y_less = by < ay

    is_target_x_less = cx < ax
    is_target_y_less = cy < ay

    if is_king_x_less == is_target_x_less and is_king_y_less == is_target_y_less:
        print("YES")
    else:
        print("NO")


solve()
