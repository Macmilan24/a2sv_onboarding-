# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        ans_idx = -1

        def val(c):
            return ord(c) - ord('a') + 1

        power_k = pow(power, k, modulo)
        
        current_hash = 0
        for i in range(n - 1, -1, -1):
            if i + k < n:
                current_hash = (current_hash - (val(s[i + k]) * power_k) % modulo + modulo) % modulo
            
            current_hash = (current_hash * power + val(s[i])) % modulo

            if i <= n - k:
                if current_hash == hashValue:
                    ans_idx = i

        n = len(s)
        power_k_minus_1 = pow(power, k - 1, modulo)
        
        current_hash = 0
        p = 1
        for j in range(k):
            i = n - k + j
            char_val = val(s[i])
            current_hash = (current_hash + char_val * p) % modulo
            if j < k - 1:
                p = (p * power) % modulo

        if current_hash == hashValue:
            ans_idx = n - k

        for i in range(n - k - 1, -1, -1):
            
            outgoing_val = val(s[i + k])
            incoming_val = val(s[i])
            
            term_to_remove = (outgoing_val * power_k_minus_1) % modulo
            current_hash = (current_hash - term_to_remove + modulo) % modulo
            current_hash = (current_hash * power) % modulo
            current_hash = (current_hash + incoming_val) % modulo

            if current_hash == hashValue:
                ans_idx = i
                
        return s[ans_idx : ans_idx + k]