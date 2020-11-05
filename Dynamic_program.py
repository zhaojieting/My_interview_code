"""
给出一个一维数组，找出结果数相加最大的选择情况，不能选相邻的元素。
三个三个一组，每次往前一组判断，四种情况，选则最大的情况，代码还未写完
"""
class Solution:
    def __init__(self):
        pass
    def maximumValue(self , arr ):
        m_value = 0
        t1_value = 0
        t2_value = 0
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return max(arr[0],arr[1])
        elif len(arr) == 3:
            return max(arr[0]+ arr[2],arr[1])
        else:
            for i in range(len(arr))[::3]:
                if i+1 == len(arr):
                    t1_value = arr[i+1] - arr[i] - arr[i-2]
                    t1_value = arr[i]
                    t1_value = arr[i] + arr[i+2]
                    t2_value = arr[i+1]