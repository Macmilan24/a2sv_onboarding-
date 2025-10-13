# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        primes = [True] * 10000
        primes[0] = primes[1] = False
        for i in range(2, int(9999**0.5) + 1):
            if primes[i]:
                for multiple in range(i*i, 10000, i):
                    primes[multiple] = False

        if primes[n]:
            return -1

        pq = [(n, n)]
        visited = {n}

        while pq:
            cost, curr_n = heapq.heappop(pq)

            if curr_n == m:
                return cost

            s_curr_n = str(curr_n)
            num_digits = len(s_curr_n)

            for i in range(num_digits):
                original_digit = int(s_curr_n[i])

                if original_digit < 9:
                    next_n = curr_n + 10**(num_digits - 1 - i)
                    if not primes[next_n] and next_n not in visited:
                        visited.add(next_n)
                        heapq.heappush(pq, (cost + next_n, next_n))

                if original_digit > 0:
                    next_n = curr_n - 10**(num_digits - 1 - i)
                    if len(str(next_n)) == num_digits and not primes[next_n] and next_n not in visited:
                        visited.add(next_n)
                        heapq.heappush(pq, (cost + next_n, next_n))
        return -1