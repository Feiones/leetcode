"""
832. 翻转图像
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                elif row[i] == 0:
                    row[i] = 1
            row.reverse()
        return A