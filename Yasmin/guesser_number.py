#####################################################################
# Jogo "Adivinhe o número!"
# criado por Yasmin Deodato
# Disponível em: http://www.codeskulptor.org/#user46_acnbNNwPIQ_12.py
#####################################################################
import simplegui
import random

# função de ajuda para iniciar um novo jogo
def new_game():
    global secret_number
    
    #numero aleatorio
    secret_number = random.randrange(0, range)
        
    print'------------NOVO JOGO------------'
    print('INTERVAL0: [0,' + str(range) + ')')
    print('PALPITES RESTANTES: ' + str(attempt) + '\n')   

# define os manipuladores de evento 
# para o painel de controle
def range100():
    # botão que muda o range para [0,100) e inicia novo jogo 
    global range
    global attempt
    range = 100
    attempt = 7
    new_game()

def range1000():
    # botão que muda o range para [0,1000) e inicia novo jogo     
    global range
    global attempt
    range = 1000
    attempt = 10
    new_game()
    
def input_guess(guess):
    global attempt
   
    #subtrai 1 palpite do numero atual de palpites
    attempt = attempt - 1
    
    #converte a entrada do usuário para int
    guess = int(guess)
    
    if(attempt >= 0):
        print'O palpite foi', guess

        if(secret_number == guess):
            resultado = 'CORRETO! | PALPITES RESTANTES: ' + str(attempt) + '\n'
            print resultado
            new_game()
            return
        elif(secret_number > guess):
            resultado = 'MAIOR'
        else:
            resultado = 'MENOR'

        resultado = resultado + ' | PALPITES RESTANTES: '  + str(attempt) + '\n'
        print resultado
    
    if(attempt == 0):
        print 'Voce nao tem mais palpites :( \nO numero era', secret_number, '\n'
        new_game()
        
# cria frame
frame = simplegui.create_frame("Adivinhe o numero", 300, 200)

# registre os manipuladores de evento para controlar os elementos e iniciar frame
frame.add_input("Digite o palpite: ", input_guess, 100)
frame.add_button("Range é \[0,100\)", range100)
frame.add_button("Range é \[0,1000\)", range1000)
frame.start()

#iniciar jogo com range 100
range100()
