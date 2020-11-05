"""
寰宇科技面试题最后一小题，较为简单，先找到元素可能位于哪一行，因为元素是顺序排列的，再判断元素是否在那一行
本题用二分思想查找元素
"""

class Solution:
    def __init__(self):
        self.flag = 0
    def searchMatrix(self , matrix , target ):

        leng = int(len(matrix) / 2)
        if leng == 0:
            if matrix[0].count(target) == 1:
                self.flag += 1
        elif matrix[leng][0] >= target:
            self.searchMatrix(matrix[:leng], target)
        else:
            self.searchMatrix(matrix[leng:], target)
        if self.flag == 1:
            return True
        else:
            return False




