"""
寰宇科技面试题第一题，对我而言较难，定义check函数，函数递归查找周边的元素，如果查找到该元素为1，并且mem显示没有被遍历过，
则self.area ++，这样一次迭代后就可以返回那片区域的面积，最终得到最大面积。
开心，自己闷头写粗来滴，吼吼吼哈哈哈哈，0.0
"""

class Solution:
    def __init__(self):
        self.area = 0
        self.mem = list()

    def check(self,i,j,grid):
        if j+1 < len(grid[0]) and grid[i][j+1] == 1 and self.mem[i][j+1] == 0:
            self.area += 1
            self.mem[i][j+1] += 1
            self.check(i,j+1,grid)
        if i+1 < len(grid) and grid[i+1][j] == 1 and self.mem[i+1][j] == 0:
            self.area += 1
            self.mem[i+1][j] += 1
            self.check(i+1,j,grid)
        if i-1 >= 0 and grid[i-1][j] == 1 and self.mem[i-1][j] == 0:
            self.area += 1
            self.mem[i-1][j] += 1
            self.check(i-1,j,grid)
        if j-1 >= 0 and grid[i][j-1] == 1 and self.mem[i][j-1] == 0:
            self.area += 1
            self.mem[i][j-1] += 1
            self.check(i,j-1,grid)
    def maxAreaOfIsland(self,grid):
        maxarea = 0
        self.area = 0
        self.mem = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and self.mem[i][j] == 0:
                    self.area = 1
                    self.mem[i][j] += 1
                    self.check(i,j,grid)
                    if self.area > maxarea:
                        maxarea = self.area
                    self.area = 0
        return maxarea

s = Solution()
print(s.maxAreaOfIsland([[1,0,0],[1,1,0]]))