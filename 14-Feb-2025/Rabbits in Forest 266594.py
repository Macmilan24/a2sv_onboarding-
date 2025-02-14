# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        answer_count = Counter(answers)

        rabbit_count = 0

        for num, freq in answer_count.items():
            number = ((freq - 1 ) // (num + 1)) + 1
            rabbit_count += number * (num + 1)
        
        return rabbit_count


        