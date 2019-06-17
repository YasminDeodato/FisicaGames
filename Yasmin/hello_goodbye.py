#Desafio 1: hello_goodbye.py
#Proposta: ao clicar no botão hello ou goodbye mostra texto correspondente.
#Disponível em: http://www.codeskulptor.org/#user46_ykK8brwZ9y_8.py
import simplegui

def print_hello():
    label.set_text('Hello')

def print_goodbye():
    label.set_text('Goodbye')

frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)
label = frame.add_label('')

frame.start()


###################################################
# Testes
'''/
print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()'''
