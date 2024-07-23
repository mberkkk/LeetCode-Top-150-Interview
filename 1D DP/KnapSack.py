'''
Bu algoritmada amacımız belirli ağırlıklara ve değerlere sahip nesneler arasından
bir sırt çantasının kapasitesini aşmadan
en yüksek değerli nesneleri sırt çantasına doldurmaya çalışmak


her bir nesnenin ağırlığı w[i]
her bir nesnenin değeri v[i]

maksimum kapasite 'W'
'''

'''
F(i,j) fonksiyonu ilk 'i' nesneyi kullanarak kapasitesi 'j' olan bir sırt çantasında 
elde edilebilecek maksimum değeri ifade eder.
'''

def knapsack(values, weights, W):
    n = len(values)
    F = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range (1,n + 1):
        for j in range (1, W + 1):
            if weights[i - 1] <= j:
                F[i][j] = max(F[i-1][j], values[i-1] + F[i-1][j-weights[i - 1]])
            else:
                F[i][j] = F[i-1][j]
                
                
    return F[n][W]


values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]
W = 15

print(knapsack(values, weights, W))


