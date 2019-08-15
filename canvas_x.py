# Mostre X
# criado por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_3oCdlH8iK9_2.py
####################################################################
import simplegui 

# Draw handler
def draw_handler(canvas):
    canvas.draw_text('X', (0, 35), 48, 'Red')
    
# Cria o frame e assinala os callbacks aos manipuladores de eventos
frame = simplegui.create_frame("X", 96, 96)
frame.set_draw_handler(draw_handler)

# Inicia o frame de animação
frame.start()
