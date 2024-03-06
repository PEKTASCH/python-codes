''' Doğum tarihinden yaşını bulan kod yapısı görülmektedir. Burda önemli olan int fonksiyonu ile birthday
değişkeni içindeki son 4 karakteri tam sayıya çeviren ve günümüzdeki yıldan çıkararak yaşını hesaplayan kod
yapısı mantığıdır'''

birthday = 'January 1, 1991'

year = int(birthday[-4: ])

print('You are', 2022 - year, 'years old.')