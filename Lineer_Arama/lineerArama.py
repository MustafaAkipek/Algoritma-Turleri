def lineer_arama(dizi, hedef):
    n = len(dizi)
    for i in range(n):
        if dizi[i] == hedef:
            return i
    return -1

print(lineer_arama([1,2,4,5,8,10],5))