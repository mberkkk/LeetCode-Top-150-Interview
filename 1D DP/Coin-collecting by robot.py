
#Bu problemde, bir robotun nxm boyutlarındaki bir tahtada yerleştirilmiş olan
#coinleri (madeni paraları) toplayarak mümkün olduğunca çok sayıda coin toplaması 
#ve sağ alt hücreye ulaşması gerekiyor. Robot sadece sağa veya aşağı hareket
#edebiliyor.

def RobotCoinCollection(board):
    n = len(board)
    m = len(board[0])
    
    # DP Tablomuzu 0 ile doldurduk
    F = [[0] * (m + 1) for _ in range(n + 1)]
    

    #DP Satırı doldurumu
    for j in range(1,m):
        #eğer solumdaki hücrede coin var ise toplaya toplaya gideceğimden ötürü
        #sağdaki hücrede toplayacağım maksimum coin; soldaki hücrede coin var ise artar
        F[0][j] = F[0][j-1] + board[0][j]
    
    
    #DP Sütunu doldurumu
    for i in range (1,n):
        F[i][0] = F[i-1][0] + board [i][0]
    
    
    
    #DP Tablosu doldurumu
    for i in range (1,n):
        for j in range(1,m):
            F[i][j] = max(F[i-1][j],F[i][j-1]) + board[i][j]
    
    
    return F[m-1][n-1]
    
board = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(RobotCoinCollection(board))