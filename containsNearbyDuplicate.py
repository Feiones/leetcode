"""
219. 存在重复元素 II
下面方法超出时间限制，
"""
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         low = 0
#         high = 1
#         # indictor = 0
#         while low < len(nums):
#             while high < len(nums):
#                 if nums[low] == nums[high]:
#                     if high - low <= k:
#                         return True
#                 high += 1
#             low += 1
#             high = low + 1
#         return False
"""
用字典存相应数值的索引
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, n in enumerate(nums):
            if n not in d or (idx - d[n]) > k:
                d[n] = idx
            else:
                return True
        else:
            return False