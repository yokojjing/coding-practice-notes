class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in matrix:
            for i in range(len(row)//2):
                row[i],row[len(row)-1-i] = row[len(row)-1-i],row[i]
        