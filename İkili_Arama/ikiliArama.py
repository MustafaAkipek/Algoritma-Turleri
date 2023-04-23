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

dizi = [2, 5, 8, 12, 16, 23, 38, 45, 67, 89]
hedef = 30
sonuc = ikili_arama(dizi, hedef)

if sonuc == -1:
    print("Hedef değer dizide bulunamadi.")
else:
    print("Hedef değer dizinin indeksi:", sonuc)
