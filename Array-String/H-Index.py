def hIndex(citations):
    if len(citations) == 1 and citations[0] > 0:
        return 1

    temp_count = 0
    temp_list = [0]
    j = 0
    for i in range(len(citations)):

        # bulunan h-indexinden daha küçük bir değeri kontrol etmemek
        if temp_list[0] != 0 and citations[i] <= temp_list[0]:
            continue
        j = 0
        while((temp_count <= citations[i]) and j < len(citations)):
            if citations[j] >= citations[i]:
                temp_count += 1
            j += 1

#        for j in range(len(citations)):
#
#            if citations[j] >= citations[i]:
#                temp_count += 1



        if temp_count >= citations[i]:
            if citations[i] > temp_list[0]:
                temp_list[0] = citations[i]
        else:
            if temp_count > temp_list[0]:
                temp_list[0] = temp_count

        temp_count = 0


    return temp_list[0]


# optimize fikirleri
# eğer listedeki sayımızdan daha küçük bir sayıyı kontrol ediyorsak kontrol etmeyebiliriz
# eğer h index için gerekli sayıya ulaşırsak listeyi boş yere dönmeyebiliriz


citations = [3, 0, 12, 1, 5,13,14,15]
print(hIndex(citations))