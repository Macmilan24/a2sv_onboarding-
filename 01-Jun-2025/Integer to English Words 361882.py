# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
                 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        scales = ["", "Thousand", "Million", "Billion"]

        result = []
        chunkIndex = 0

        while num > 0:
            chunk = num % 1000
            if chunk != 0:
                chunkWords = []
                hundreds = chunk // 100
                remainder = chunk % 100

                if hundreds > 0:
                    chunkWords.append(ones[hundreds - 1] + " Hundred")

                if 10 <= remainder < 20:
                    chunkWords.append(teens[remainder - 10])
                else:
                    tensPlace = remainder // 10
                    onesPlace = remainder % 10

                    if tensPlace > 1:
                        chunkWords.append(tens[tensPlace - 2])
                    if onesPlace > 0:
                        chunkWords.append(ones[onesPlace - 1])

                if scales[chunkIndex]:
                    chunkWords.append(scales[chunkIndex])

                result.append(' '.join(chunkWords))

            num //= 1000
            chunkIndex += 1

        return ' '.join(reversed(result))