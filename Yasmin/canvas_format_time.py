# Função que retorna o número formatado em minutos e segundos
# criada por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_AeovuqOjJl_8.py
####################################################################
import random
import simplegui

time = ''
# Função de formatação do tempo
def format_time(input):
    global time
    input = int(input)
    if input >= 3600:
        time = "%sh %smin %ss"%(input/3600, input%3600/60, input%3600%60)
    else:
        time = "%smin %ss"%(input/60, input%60)
    
    print time
    
def random_number():
    return random.randrange(0, 3600)
    
# Handler to write on canvas
def draw(canvas):
    global time
    canvas.draw_text(time, [50, 100], 28, "White")
    
# Cria um frame
frame = simplegui.create_frame("Conversao de Segundos", 300, 200)
frame.add_input("Digite o tempo em segundos e aperte enter: ", format_time, 100)

frame.set_draw_handler(draw)
frame.start()

###################################################
# Testes

'''print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)'''

###################################################
# Saída no console
#0 minutos e 23 segundos
#20 minutos e 37 segundos
#0 minutos e 0 segundos
#31 minutos e 0 segundos
