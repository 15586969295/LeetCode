# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if (target - i) in nums:
                if i != (target - i):
                    return [nums.index(i), nums.index(target - i)]
                else:
                    if nums.count(i) > 1:
                        a = nums.index(i)
                        nums[nums.index(i)] += 1
                        b = nums.index(i)
                        return [a, b]
