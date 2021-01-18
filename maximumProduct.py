"""
628. 三个数的最大乘积
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积
想法：对一个数组进行排列，三个数的最大只出现的地方分两种：
    若数组中存在多个负数，则最大值要么是前两个数加最后一个数的乘积，要么是最后三个数的乘积
"""
class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        res = 1
        for i in nums[-1:-4:-1]:
            res *= i
        if nums[0]*nums[1]*nums[len(nums)-1] > res:
            res = nums[0]*nums[1]*nums[len(nums)-1]
        return res