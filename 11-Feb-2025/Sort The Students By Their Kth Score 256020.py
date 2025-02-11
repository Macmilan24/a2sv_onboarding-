# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n = len(score)

        kth_exam = []

        for i in range(n):
            kth_exam.append((score[i][k], i))
        
        kth_exam.sort(reverse = True)

        ans = []
        for _ , i in kth_exam:
            ans.append(score[i])
        
        return ans