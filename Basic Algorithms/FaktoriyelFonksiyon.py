def faktoriyel(n):       # Fonksiyon kullanarak faktoriyel hesabı yapan program
    
    if n == 0:           # 0! = 1 olduğundan ekstra eklendi.
        return 1         
    
    else:
        return n * faktoriyel(n-1)

num = int(input("Bir pozitif sayi sayi girin: "))

print("Faktöriyel: ", faktoriyel(num))