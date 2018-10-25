# Given two arrays, write a function to compute their intersection.
# 给定两个数组，编写一个函数来计算它们的交集。


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1 and lst.count(i) < nums1.count(i):
                    lst.append(i)
        else:
            for i in nums1:
                if i in nums2 and lst.count(i) < nums2.count(i):
                    lst.append(i)
        return lst
