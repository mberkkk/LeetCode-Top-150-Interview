# Amacımız hedeflenen değere kadar her değeri en kısa şekilde bularak hedefe ulaşmak



def coinChange(coins, amount):
    if not coins:
        return 0
    #For döngümüz hedeflenen değer kadar döneceğinden o değerin bir fazlası kadar infinite liste oluşturuyoruz
    F = [amount + 1] * (amount + 1)
    # amount + 1 infinite'i temsil ediiyor çünkü target değerinden daha büyük bir adette targeti bulmamız olanaksız.
    
    
    F[0] = 0
    for i in range(1, amount + 1):
        # amounttaki her değer için o değere coinlerle nasıl ulaşacağımıza bakıyoruz.
        for coin in coins:
            # bizim 'current' hedef değerimizden büyük bir coin varsa o coinle işlem yapamayacağımız için almıyoruz.
            if coin <= i:
                #F[i - coin] 'current' hedef değerinden coin değerini çıkardığımızdaki değere kaç adımda ulaşacağımızdır
                #Mesela 6 targetinde 5 coinini kullanırsak yeni hedefimiz 1 e ulaşmaktır
                #Her yeni coinle işlem yapıldığında kullanılan coin sayısı arttığından +1 gelmekte.
                    
                F[i] = min(F[i] , F[i - coin] + 1)
    
    if F[-1] == amount +1:
        
        return -1
    
    else:
        return F[-1]

    
coins = [1,2,3] 
amount = 6

print(coinChange(coins,amount))