"""
1550. 存在连续三个奇数的数组
最直观的想法就是每三个三个连续的元素进行遍历，判断是否是奇数
"""
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr)-2):
            if (arr[i] % 2 != 0) and (arr[i+1] % 2 != 0) and (arr[i+2] % 2 != 0):
                return True
        return False