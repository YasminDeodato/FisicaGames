# Jogo da Cobrinha
# Criado por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_xTrdhFy2r3_1.py
####################################################################
import simplegui
import random
import math

# inicializa as variáveis globais
LARGURA = 600
ALTURA = 400

COMIDA_RAIO = 10
comida_pos = [0, 0]

BOLA_RAIO = 12

cabeca = [LARGURA/2, ALTURA/2]
corpo = []

jogo = True
mensagem = ''
pontuacao = 0

const = 5
vel = [0, 4]

# Handler p/ os botões 
def iniciar():
    global comida_pos, cabeca, corpo, jogo, mensagem, pontuacao, const, vel
    
    comida_pos = [LARGURA/2, ALTURA/4]
    
    cabeca = [LARGURA/2, ALTURA/2]
    corpo = []
 
    jogo = True
    mensagem = ''
    pontuacao = 0
    
    const = 5
    vel = [0, 0]
    
def pausar():
    global jogo
    if jogo == True:
        jogo = False 
    else:
        jogo = True
    
# Posição aleatória da comida    
def comidaPosicao():
    global comida_pos
    comida_pos[0] = random.randrange(BOLA_RAIO, LARGURA - BOLA_RAIO)
    comida_pos[1] = random.randrange(BOLA_RAIO, ALTURA - BOLA_RAIO)
    
# Draw handler 
def draw(canvas):
    global cabeca, corpo, cobra, comida_pos, pontuacao, mensagem, vel
         
    if jogo == True:
        # verifica se há colisão
        colisao()
        
        # verifica se a cobra comeu a comida
        comeuComida()
               
        # atualiza posição dos gomos do corpo
        if corpo: 
            # move os gomos em ordem reversa
            for index in range(len(corpo) - 1, 0, -1):                        
                        x = corpo[index - 1][0] - 2 * BOLA_RAIO * vel[0]
                        y = corpo[index - 1][1] - 2 * BOLA_RAIO * vel[1]
                        corpo[index] = [x, y]
                        
            # move o primeiro segmento do corpo p/ posicao da cabeca 
            if len(corpo) > 0:
                corpo[0] = [cabeca[0] - 2 * BOLA_RAIO * vel[0], cabeca[1] - 2 * BOLA_RAIO * vel[1]]
        
        # atualiza a posição da cabeça da cobra
        mover()
        
    
    # escreve a pontuação 
    canvas.draw_text('Pontos: ' + str(pontuacao), (5, 20), 24, 'White')
    
    # escreve a mensagem 
    canvas.draw_text(mensagem, (LARGURA/3, ALTURA/2), 24, 'Red')
    
    # desenha o corpo da cobra
    if corpo:
        for gomo in corpo:
            canvas.draw_circle(gomo, BOLA_RAIO, 1, "White", "White")
           
    # desenha a cabeça da cobra
    canvas.draw_circle(cabeca, BOLA_RAIO, 1, "Green", "Green")
        
    # desenha a comida
    canvas.draw_circle(comida_pos, COMIDA_RAIO, 1, "red", "red")

# Move a cabeça da cobra
def mover():
    global cabeca, corpo, vel   
        
    cabeca[0] += vel[0]
    cabeca[1] += vel[1]
    
# Verifica se a cobra comeu a comida
def comeuComida():
    global cabeca, corpo, comida_pos, pontuacao, const
    
    if len(corpo) < 1:
        gomo_anterior = cabeca
    else: 
        gomo_anterior = corpo[len(corpo) - 1]
    
    # calcula a distancia entre a cabeça da cobra e a comida
    distancia = math.sqrt(((cabeca[0]-comida_pos[0])**2)+((cabeca[1]-comida_pos[1])**2))   
    
    # se a cobra tangencia a comida
    if distancia <= BOLA_RAIO + COMIDA_RAIO:
        # adiciona um novo gomo no corpo da cobra
        corpo.append([gomo_anterior[0] + 2 * BOLA_RAIO, gomo_anterior[1] + 2 * BOLA_RAIO])

        # atualiza a posição da comida
        posicaoComida()
        
        # atualiza a pontuação
        pontuacao += 10
        
    
# Posição aleatória da comida    
def posicaoComida():
    global comida_pos
    comida_pos[0] = random.randrange(COMIDA_RAIO, LARGURA - COMIDA_RAIO)
    comida_pos[1] = random.randrange(COMIDA_RAIO, ALTURA - COMIDA_RAIO)

# Colisão    
def colisao():
    global cabeca, corpo, mensagem, jogo
    
    if corpo: 
        ultimo_gomo = corpo[len(corpo)-1]
    else:    #se o corpo estiver vazio, o ultimo_gomo será a cabeça
        ultimo_gomo = cabeca
        
    primeiro_gomo = cabeca
    
    # colisão com as paredes
    if primeiro_gomo[0] > LARGURA - (BOLA_RAIO + 1) or ultimo_gomo[0] > LARGURA - (BOLA_RAIO + 1):
        jogo = False
    elif primeiro_gomo[0] < BOLA_RAIO + 1 or ultimo_gomo[0] < BOLA_RAIO + 1:
        jogo = False
    elif primeiro_gomo[1] < BOLA_RAIO + 1 or ultimo_gomo[1] < BOLA_RAIO + 1:
        jogo = False
    elif primeiro_gomo[1] > ALTURA - (BOLA_RAIO + 1) or ultimo_gomo[1] > ALTURA - (BOLA_RAIO + 1):
        jogo = False
    
    # colisão com o próprio corpo
    if primeiro_gomo[0] == ultimo_gomo[0] and primeiro_gomo[1] == ultimo_gomo[1] - BOLA_RAIO:
        jogo = False
    
    # atualiza mensagem
    if jogo == False:
        mensagem = 'Fim de Jogo'

# Evento do teclado
def keydown(key):
    global vel, const
    if key == simplegui.KEY_MAP["right"]:
        vel = const * [1,0]
    if key == simplegui.KEY_MAP["left"]:
        vel = const * [-1,0]
    if key == simplegui.KEY_MAP["up"]:
        vel = const * [0,-1]
    if key == simplegui.KEY_MAP["down"]:
        vel = const * [0,1]
    if key == simplegui.KEY_MAP["space"]:
        pausar()
        
# Cria o frame
frame = simplegui.create_frame("Jogo da Cobrinha", LARGURA, ALTURA)
# Adiciona os componentes da tela
frame.add_label("Jogo da Cobrinha")
frame.add_button("Iniciar Jogo", iniciar)
frame.add_button("Pausar Jogo", pausar)

# Registra os handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Inicia o frame
iniciar()
frame.start()
