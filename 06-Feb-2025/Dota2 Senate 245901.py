# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        senate = list(senate)

        D, R = deque(), deque()

        for i , char in enumerate(senate):
            if char == "R":
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            rTurn = R.popleft()
            dTurn = D.popleft()
            
            if rTurn < dTurn :
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        
        return "Radiant" if R else "Dire"
         
        