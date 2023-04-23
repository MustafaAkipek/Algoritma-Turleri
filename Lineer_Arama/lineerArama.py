def lineer_arama(dizi, hedef):
    n = len(dizi)
    for i in range(n):
        if dizi[i] == hedef:
            return i
    return -1

dizi = [1,2,4,5,8,10]
hedef = 5
print(lineer_arama(dizi,hedef))