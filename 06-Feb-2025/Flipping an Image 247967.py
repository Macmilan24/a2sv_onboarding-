# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()

            for i in range(len(img)):
                if img[i] == 1:
                    img[i] = 0
                else:
                    img[i] = 1
        
        return image
        