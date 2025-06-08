# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            n1_str = num[0:i]
            if len(n1_str) > 1 and n1_str.startswith('0'):
                break

            for j in range(i + 1, n):
                n2_str = num[i:j]
                if len(n2_str) > 1 and n2_str.startswith('0'):
                    break
                
                if max(len(n1_str), len(n2_str)) > n - j:
                    break
                
                first = int(n1_str)
                second = int(n2_str)
                current_idx = j
                
                while current_idx < n:
                    sum_val = first + second
                    sum_str = str(sum_val)
                    
                    if not num.startswith(sum_str, current_idx):
                        break
                    
                    current_idx += len(sum_str)
                    first, second = second, sum_val
                else:
                    if current_idx == n:
                        return True
                        
        return False