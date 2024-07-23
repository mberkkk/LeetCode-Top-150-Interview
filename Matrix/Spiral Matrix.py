class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        output = [matrix[0][0]]
        index = [[0,0]]
        x = len(matrix)
        y = len(matrix[0])
        i = 0
        j = 0
        count = 1

        while(count < x * y):
            
            while (j + 1 < y  and [i,j+1] not in index):
                output.append(matrix[i][j+1])
                index.append([i,j+1])
                j += 1
                count += 1
            
            while (i + 1 < x  and [i+1,j] not in index):
                output.append(matrix[i+1][j])
                index.append([i+1,j])
                i += 1                 
                count += 1
            
            while (j > 0 and[i,j-1] not in index):
                output.append(matrix[i][j-1])
                index.append([i,j-1] )
                j-= 1     
                count += 1

            while (i > 0 and [i-1,j] not in index):
                output.append(matrix[i-1][j])
                index.append([i-1,j])
                i -= 1                 
                count += 1
                    
        return output
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
solution = Solution()
print(solution.spiralOrder(matrix))