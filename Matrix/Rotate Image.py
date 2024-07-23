class Solution(object):
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range (i,(len(matrix))):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix

    def rotate(self, matrix):
        matrix = self.transpose(matrix)
        rowLength = len(matrix)

        for i in range(len(matrix)):
            l = 0
            r = rowLength - 1
            while (l <= r):
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp

                l += 1
                r -= 1

        return matrix
        
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution = Solution()
print(solution.rotate(matrix))

