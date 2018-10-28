# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1.Each row must contain the digits 1-9 without repetition.
# 2.Each column must contain the digits 1-9 without repetition.
# 3.Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
# 1.数字 1-9 在每一行只能出现一次。
# 2.数字 1-9 在每一列只能出现一次。
# 3.数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        raw = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        cell = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            for j in range(9):
                num = (3 * (i // 3) + j // 3)
                temp = board[i][j]
                if temp != ".":
                    if temp not in raw[i] and temp not in col[j] and temp not in cell[num]:
                        raw[i][temp] = 1
                        col[j][temp] = 1
                        cell[num][temp] = 1
                    else:
                        return False
        return True


test_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(test_board))
