#Desafio 2: colors.py
#Proposta: clicar nos botões azul e vermelho para manipular variável color e mostrar na tela.
#Disponível em: http://www.codeskulptor.org/#user46_6fWg1Sa0oo_4.py
import simplegui

def set_red():
    global color
    color = "red"


def set_blue():
    global color
    color = "blue"


def print_color():
    label.set_text(color)
    print
    color


frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button("Color 1", set_red)
frame.add_button("Color 2", set_blue)
frame.add_button("Print Color", print_color)
label = frame.add_label('')

frame.start()

###################################################
# Teste
'''/
set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()'''
###################################################
# Resultados esperados do teste

# red
# blue
# blue
