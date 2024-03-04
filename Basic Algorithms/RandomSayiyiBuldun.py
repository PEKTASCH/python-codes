from random import randint

i = 0

s = randint(1,20)       # 1-20 arası rastege bir sayı üretilsin (20 dahil değil)

while i < 34:
    
    t = eval(input('t:'))    # Eğer kullanıcının girdiği sayı random üretilen sayıya eşitse ekranda Buldun yazdır
        
    if s == t:
            
        print('Buldun')
                
        break