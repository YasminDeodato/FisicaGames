# Jogo da Cobrinha
# Criado por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_6T6NT98Pnh_4.py
####################################################################
import simplegui
import random

# inicializa as variáveis globais
LARGURA = 600
ALTURA = 600

# Handler p/ os botões 
def iniciar():
    global cabeca, cobra, vel, comida, jogo, mensagem, pontuacao
    
    timer_reiniciar.stop()
    timer.start()
    
    cabeca = [140, 60]
    cobra = [[cabeca[0] - 80, cabeca[1]],[cabeca[0] - 40 ,cabeca[1]], cabeca]
    vel = [1, 0]
    posicaoComida()
    jogo = True
    mensagem = ' '
    pontuacao = 0
    
def pausar():
    global jogo
    if jogo:
        jogo = False 
    else:
        jogo = True

# Handler do timer
def timer_handler():
    global cabeca, vel, comida, cobra, pontuacao, jogo, mensagem, timer_reiniciar
    
    if jogo:
        if cabeca[0] == comida[0] and cabeca[1] == comida[1]:
            # adiciona um novo gomo no corpo da cobra
            cobra.append(list(comida))
            
            # atualiza a posição da comida
            posicaoComida()
        
            # atualiza a pontuação
            pontuacao += 10
        else:
            # atualiza a posição da cabeca
            cabeca[0] += 40*vel[0]
            cabeca[1] += 40*vel[1]
            
            cobra.append(list(cabeca))
            cobra.pop(0)
       
        # verifica se há colisão da cobra
        colisao()
     
    if jogo == False and mensagem == 'Fim de Jogo.':
        timer_reiniciar.start()
        
def timer_reiniciar():
    timer.stop()
    iniciar()
    
# Posição aleatória da comida    
def posicaoComida():
    global comida, cobra
    
    nao_deu_certo = True
    semente = [-1,-1]
    
    while nao_deu_certo:
        semente[0] = random.randrange(60, 560, 40)
        semente[1] = random.randrange(60, 560, 40)
        
        if semente not in cobra:
            nao_deu_certo = False
            comida = semente
    
# Draw handler 
def draw(canvas):
    global cobra, mensagem, pontuacao 
    
    # Desenha as linhas guias
    '''for i in range(16):           
        canvas.draw_line([0,0 + 40*i], [LARGURA, 0 + 40*i], 2, "White")
        canvas.draw_line([0 + 40*i,0], [0 + 40*i, ALTURA], 2, "White")'''
         
    # Desenha corpo
    if cobra:
        for gomo in cobra:
            #cabeça
            if cobra.index(gomo) == len(cobra)-1:
                canvas.draw_polygon([(gomo[0]-20, gomo[1]-20), 
                                 (gomo[0]-20, gomo[1]+20), 
                                 (gomo[0]+20, gomo[1]+20), 
                                 (gomo[0]+20, gomo[1]-20)], 2, 'White', 'Red')
            #corpo
            else:
                canvas.draw_polygon([(gomo[0]-20, gomo[1]-20), 
                                     (gomo[0]-20, gomo[1]+20), 
                                     (gomo[0]+20, gomo[1]+20), 
                                     (gomo[0]+20, gomo[1]-20)], 2, 'White', 'White')
        
    # desenha a comida
    canvas.draw_polygon([(comida[0]-20, comida[1]-20), 
                         (comida[0]-20, comida[1]+20), 
                         (comida[0]+20, comida[1]+20), 
                         (comida[0]+20, comida[1]-20)], 2, 'White', 'Green')
    
    # escreve a pontuação 
    canvas.draw_text('Pontos: ' + str(pontuacao), (5, 30), 30, 'White')
    
    # escreve a mensagem 
    canvas.draw_text(mensagem, (LARGURA/3, ALTURA/2), 48, 'Red')
    
# Colisão    
def colisao():
    global cobra, mensagem, jogo, cabeca
    
    ultimo_gomo = cobra[len(cobra)-1]
    primeiro_gomo = cobra[0]
    
    #colisão com as paredes
    if primeiro_gomo[0] + 40 > LARGURA or ultimo_gomo[0] + 40 > LARGURA:
        jogo = False
    elif primeiro_gomo[0] - 40 < 0 or ultimo_gomo[0] - 40 < 0:
        jogo = False
    elif primeiro_gomo[1] - 40 < 0 or ultimo_gomo[1] - 40 < 0:
        jogo = False
    elif primeiro_gomo[1] + 40 > ALTURA or ultimo_gomo[1] + 40 > ALTURA:
        jogo = False
    
    # colisão com o próprio corpo
    if primeiro_gomo[0] - 40 == ultimo_gomo[0] and primeiro_gomo[1] == ultimo_gomo[1] \
        or primeiro_gomo[0] + 40 == ultimo_gomo[0] and primeiro_gomo[1] == ultimo_gomo[1]:
        jogo = False
    
    # atualiza mensagem
    if jogo == False:
        mensagem = 'Fim de Jogo.'
        
# Evento do teclado
def keydown(key):
    global vel, jogo
    
    if jogo:
        if key == simplegui.KEY_MAP["right"]:
            jogo = True
            vel = [1,0]
        if key == simplegui.KEY_MAP["left"]:
            jogo = True
            vel = [-1,0]
        if key == simplegui.KEY_MAP["up"]:
            jogo = True
            vel = [0,-1]
        if key == simplegui.KEY_MAP["down"]:
            jogo = True
            vel = [0,1]
    if key == simplegui.KEY_MAP["space"]:
        pausar()
        vel = [0,0]

# Cria o frame
frame = simplegui.create_frame("Jogo da Cobrinha", LARGURA, ALTURA)
# Adiciona os componentes da tela
frame.add_label("Jogo da Cobrinha")
frame.add_button("Iniciar Jogo", iniciar)
frame.add_button("Pausar Jogo", pausar)

# Registra os handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Registra um timer
timer = simplegui.create_timer(250, timer_handler)
timer.start()
timer_reiniciar = simplegui.create_timer(2000, timer_reiniciar)

# Inicia o frame
iniciar()
frame.start()
