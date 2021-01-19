"""
605. 种花问题
个人觉得这道题并不简单，对于新手来说还是比较难得吧（可能是现在自己比较菜），这道题考虑的情况
比较多，if语句和continue的应用比较关键，刚开始想的时候，对于continue的应用自己根本没想到
之后也是看了题解才发现可以这样想
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            if i + 1 < m and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False
