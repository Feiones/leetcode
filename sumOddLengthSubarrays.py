"""
1588. 所有奇数长度子数组的和
"""
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        length = len(arr)
        res = 0
        # 找出每一个奇数长度的子序列，并求和
        for i in range(length):
            j = i
            while  j < length:
                res = res + sum(arr[i:j+1])
                j += 2
        return res