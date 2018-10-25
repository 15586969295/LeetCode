# Given a 32-bit signed integer, reverse digits of an integer.
# 给定一个 32 位有符号整数，将整数中的数字进行反转。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            a = int(str(x)[::-1])
        else:
            a = 0 - int(str(0 - x)[::-1])
        if -2 ** 31 < a < 2 ** 31 - 1:
            return a
        else:
            return 0
