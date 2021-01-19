"""
1275. 找出井字棋的获胜者
这个题目刚开始看有点难理解，后来明白了，这里建立两个列表分别存A和B的轨迹点
然后分别取出两个轨迹，三点一线的条件是，中间点的横纵位置点的坐标是两边点的横纵坐标和的一半
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a = []
        b = []
        for i in range(len(moves)):
            if i % 2 == 0:
                a.append(moves[i])
            else:
                b.append(moves[i])
        # print(a)
        # print(b)
        for i in a:
            for j in a:
                if i != j:
                    x = (i[0]+j[0])/2
                    y = (i[1]+j[1])/2
                    if [x,y] in a:
                        return "A"
        for i in b:
            for j in b:
                if i != j:
                    x = (i[0]+j[0])/2
                    y = (i[1]+j[1])/2
                    if [x,y] in b:
                        return "B"

        if len(moves) < 9:
            return "Pending"
        return "Draw"