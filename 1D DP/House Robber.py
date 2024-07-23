def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # F Fonksiyonunun son elemanı bize lazım o yüzden nums uzunlugunda bir liste oluşturduk
    F = [0] * len(nums)
    
    F[0] = nums[0]
    F[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        # Yeni eklenen eleman ile 2 önceki fonksiyondan gelen değer toplamı 
        # ile bir önceki fonksiyonun değer toplamı ile karşılaştırılması
        F[i] = max(nums[i] + F[i-2], F[i-1])
        
    return F[-1]

nums = [1, 2, 3, 1]
print(rob(nums))
