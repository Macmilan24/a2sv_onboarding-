# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def build_max_heap(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

        
        while len(stones) > 1:
            build_max_heap(stones)
            first = stones.pop(0)
            build_max_heap(stones)
            second = stones.pop(0)
            if first != second:
                stones.append(abs(first - second))

        return stones[0] if stones else 0