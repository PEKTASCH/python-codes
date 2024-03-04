# Girilen 5 sayının ortalamasını bulan algoritma / Finding the average of 5 entered numbers

t = 0

i = 0

while i < 5:
    
    n = eval(input('N:'))
        
    t = t + n
        
    i += 1
    
ort = t / 5

print(ort)