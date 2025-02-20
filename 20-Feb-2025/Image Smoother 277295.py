# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m = len(img)
        n = len(img[0])

        smooth = [[0] * n for _ in range(m)]

        for i in range(m): 
            for j in range(n):

                totalSum = 0
                count = 0

                for x in range(max(0, i - 1), min(m, i+2)):
                    for y  in range(max(0, j - 1), min(n, j+2)):

                        totalSum += img[x][y]
                        count += 1

                smooth[i][j] = totalSum // count
        
        return smooth