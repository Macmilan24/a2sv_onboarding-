# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_list = list(s)
        n = len(s)

        shift_array = [0] * (n + 1)

        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            shift_array[start] += shift 
            shift_array[end + 1] -= shift
        
        cur_shift = 0

        for i in range(n):
            cur_shift += shift_array[i]

            char_val = ord(s_list[i]) - ord('a')

            new_val = (char_val + cur_shift) % 26

            s_list[i] = chr(ord('a') + new_val)
        
        return "".join(s_list)