# Given an array, rotate the array to the right by k steps, where k is non-negative.
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            del nums[-1]
