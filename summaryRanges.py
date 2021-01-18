"""
228. 汇总区间
想法：
    最直观的办法就是遍历列表，只要后一个元素比前一个元素大一，则就和前面的元素组成新的数组tmp，
    直到条件大一个的条件不成立时，将输出形式调整成指定输出格式，并append进结果数组，再将tmp数组
    清空，将之前条件不成立的元素append进tmp，开始之后的遍历

    方法虽然蠢，但是比较好理解，对于新手来说比较友好，一步一步实现下来，对于新手来说还是有很多的坑的
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        if len(nums) == 1:
            a = "%d" % nums[0]
            res.append(a)
            return res
        i = 1
        tmp = [nums[0]] # 将数组的第一个元素先放进临时数组中
        while i < len(nums):
            if nums[i] - nums[i-1] == 1:
                tmp.append(nums[i])   # 当当前元素比前面的元素大1成立则将其加入临时数组中
            # 当大一个的条件不成立的时候
            else:
                if len(tmp) == 1: # 判断临时数组中元素个数，并调整输出格式
                    tmp_string = "%d" % tmp[0]
                else:
                    tmp_string = "%d->%d" % (tmp[0], tmp[len(tmp)-1])
                res.append(tmp_string) # 加入结果数组之中
                tmp.clear()
                tmp = [nums[i]]  # 注意，清空临时数组之后，需要将当前元素加入临时数组作为第一个元素
                                 #用于后续的判断
            i += 1
        # 当数组遍历完之后，需要判断临时数组的情况
        if len(tmp) == 1:
            s = "%d" % tmp[0]
        else:
            s = "%d->%d" % (tmp[0], tmp[len(tmp)-1])
        res.append(s)
        return res