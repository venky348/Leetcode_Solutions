class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroes = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes[i][j] = True

        for i in range(m):
            for j in range(n):
                if zeroes[i][j]:
                    for p in range(n):
                        matrix[i][p] = 0
                    for p in range(m):
                        matrix[p][j] = 0