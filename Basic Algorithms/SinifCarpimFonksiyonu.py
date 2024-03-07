class Example:
    
    def __init__(self, a, b):
        
        self.a = a
        
        self.b = b
        
    def add(self):
        
        return self.a + self.b
    
    def çarp(self):                          # çarpım fonksiyonu ekledim
        
        return self.a * self.b
    
e = Example(8,6)

print(e.add())

print(e.çarp())