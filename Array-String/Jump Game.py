def canJump(nums):
    list = []
    boolean = False

    for i in range(len(nums) - 1):
        if nums[i] == 0:
            list.append(i)

    if len(list) == 0:
        return True

    # listedeki 0'ların indexini tutup eğer listede 0'a kadar olan elemanlardan herhangi biri 0'a gelen indexten büyükse
    # zıplayabilir
    for i in range(len(nums) - 1):
        # index out of range'den kaçmak için
        if i > len(list) - 1:
            break
        boolean = False
        for j in range(list[i]):
            #engeli aşmam için gerekli büyüklük kontrolü
            if nums[j] > list[i] - j:
                boolean = True
        # Eğer ilk engeli aşamadıysam diğerlerine bakmama gerek yok
        if boolean == False:
            return boolean

nums = [3,2,1,0,4]
print (canJump(nums))
        