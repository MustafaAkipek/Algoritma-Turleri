def ikili_arama(dizi, hedef):
    baslangic = 0
    son = len(dizi) - 1
    
    while baslangic <= son:
        orta = (baslangic + son) // 2 # orta elemanın indeksini hesapla
        
        if dizi[orta] == hedef:
            return orta # hedef değeri bulunduğunda orta elemanın indeksini döndür
        
        if dizi[orta] < hedef:
            baslangic = orta + 1 # hedef değer ortadan büyükse sağ yarıyı ele al
        else:
            son = orta - 1 # hedef değer ortadan küçükse sol yarıyı ele al
            
    return -1 # hedef değeri dizide bulunamadığında -1 döndür

dizi = [1,4,9,10,22,30,35,43,45]
hedef = 10
print(ikili_arama(dizi,hedef))