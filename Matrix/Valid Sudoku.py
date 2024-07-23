class Solution(object):

    # Satırın geçerliliğini kontrol ediyoruz
    # Set fonksiyonu unique bir küme oluşturur
    def isRowValid(self, board):
        for row in board:
            res = set()
            for i in row:
                if i != ".":
                    if i in res:
                        return False
                    else:
                        res.add(i)
        return True


    # zip fonksiyonu matrisin transpozunu oluşturmaya yarar
    # * ifadesi bir liste veya tuple'ın içeriğini argüman olarak alır mesela 
    # mylist = [1,2,3] print(*mylist) = 1 2 3 

    def isColValid(self, board):
        for col in zip(*board):
            res = set()
            for j in col:
                if j != ".":
                    if j in res:
                        return False
                    else:
                        res.add(j)
        return True

    # Kareleri kontrol etmek için bu şekilde bir döngü kullanıldı
    # (0,0) sol üst kare (0.3) orta üst kare gibi gibi
    # sonra her kare için yine for döngüsüyle kareleri ayrı ayrı döndük
    def isSquareValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                res = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        value = board[x][y]
                        if value != ".":
                            if value in res:
                                return False
                            else:
                                res.add(value)
        return True

    def isValidSudoku(self, board):
        return  (self.isRowValid(board) and 
                 self.isColValid(board) and 
                 self.isSquareValid(board))


 
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print(solution.isValidSudoku(board))
