print("""
İşlem Listesi

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
""")
while True:
    islem = input("İşlem Seçiniz (İptal etmek için için 'q' tuşuna basiniz): ")
    
    if islem == 'q':
        print("İptal edildi.")
        quit()
    
    elif islem == "1":
        print("Toplama İşlemi")
        sayi1 = int(input("1. Sayiyi Giriniz: "))
        sayi2 = int(input("2. Sayiyi Giriniz: "))
        print("{}  +   {}    =  {}".format(sayi1, sayi2, sayi1+sayi2))
    
    elif islem == "2":
        print("Çikarma İşlemi")
        sayi1 = float(input("1. Sayiyi Giriniz: "))
        sayi2 = float(input("2. Sayiyi Giriniz: "))
        print("{}  -   {}    =  {}".format(sayi1, sayi2, sayi1-sayi2))
    
    elif islem == "3":
        print("Çarpma İşlemi")
        sayi1 = float(input("1. Sayiyi Giriniz: "))
        sayi2 = float(input("2. Sayiyi Giriniz: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
    
    elif islem == "4":
        print("Bölme İşlemi")
        
        try:
            sayi1 = int(input("1. Sayiyi Giriniz: "))
            sayi2 = int(input("2. Sayiyi Giriniz: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        
        except ZeroDivisionError:               # Bölme işleminde kullanıcı paydaya 0 yazarsa hata olmasını sağlamak için exception(istisna) üretmesine yol açmalıyım.
            print("Bir sayiyi 0'a bölemezsiniz!")  
        
        except ValueError:
            print("Lütfen sadece sayı girin!")  # int türünde olmayan bir DEĞERİ girerse de hata almalı 
    
    else:
        print("Geçersiz Seçenek...")