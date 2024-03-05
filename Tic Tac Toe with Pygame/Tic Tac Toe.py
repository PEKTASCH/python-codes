from pygame import *
from pygame.sprite import *

pygame.init()
screen = display.set_mode((width, height))
display.set_caption("Oyun Penceresi Başliği")  # Daha sonra değiştirilecek

while True:

    e = event.wait()             # Oyunu durdurma eventi
    if e.type == QUIT:           #pyGame'i kapatmak için kullandığım if yapısı
        pygame.quit()
        break
    screen.fill((255,255,255))   # Oyun penceresi için BEYAZ renk arka plan kodum
    display.update