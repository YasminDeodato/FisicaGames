# Muda a bola
# criado por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_mkR69cOCDy_3.py
####################################################################
import simplegui 

# Definição de globais
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    if(ball_radius > 0):
        canvas.draw_circle((200, 200), ball_radius, 5, 'Orange', 'Yellow')

# Event handlers e botões
def increase_radius():
    global ball_radius
    ball_radius = ball_radius + RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    ball_radius = ball_radius - RADIUS_INCREMENT
    
    if(ball_radius <= 0):
        ball_radius = 1

# Cria o frame e assinala os callbacks aos manipuladores de eventos
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)

# Inicia o frame de animação
frame.start()
