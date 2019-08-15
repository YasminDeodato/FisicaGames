# Print para o canvas
# criado por Yasmin Deodato
# disponível em: http://www.codeskulptor.org/#user46_MRJC8yTojD_2.py
####################################################################
import simplegui 

# Handler para o desenho (draw)
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    
# Cria o frame e assinala os callbacks aos manipuladores de eventos
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)
frame.start()

