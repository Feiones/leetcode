"""
1331. 数组序号转换
根据每一个元素的大小确定元素的序号
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr) # 确定元素的个数（重复元素算成是一个元素）
        l = list(s) # 转成一个新的列表
        l.sort() # 对列表进行排序
        d = {}
        for i in range(len(l)):
            d[l[i]] = i+1 # 确定每一个元素的序号
        return [d[j] for j in arr] # 按照原来列表的元素排列顺序输出每一个元素的序号