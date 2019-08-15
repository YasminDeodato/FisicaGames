# Mostre "Isso é fácil?"
# criado por Yasmin Deodato
# disponível em: http://www.codeskulptor.org/#user46_RQ7Mf8JegU_2.py
####################################################################
import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("Isso eh facil?",[70, 112], 48, "Red")

# Cria o frame e assinala os callbacks aos manipuladores de evento
frame = simplegui.create_frame("Isso e facil", 400, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

