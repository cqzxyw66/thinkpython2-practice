class Solution:
    def romanToInt(self, s: str) -> int:
        from itertools import pairwise
        new_dict = {'I':1, 'V':5, 
                    'X':10, 'L':50, 
                    'C':100, 'D':500, 
                    'M':1000}
        ans = 0
        for x, y in pairwise(s):  # 遍历 s 中的相邻字符
            x, y = new_dict[x], new_dict[y]
            # 累加 x 或者 -x，这里 y 只是用来辅助判断 x 的正负
            ans += x if x >= y else -x
        return ans + new_dict[s[-1]]  # 加上最后一个罗马数字
    
a = 'DCXXI'
print(Solution().romanToInt(a))