# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in range(len(matrix)):
            temp.append(list())
            for lst in temp:
                for j in range(len(matrix)):
                    lst.append("")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp[j][len(matrix) - i - 1] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp[i][j]
