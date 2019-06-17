#Desafio 3: count.py
#Proposta: manipular valores de count, através dos botões e mostrar na tela.
#Disponível em: http://www.codeskulptor.org/#user46_Gz2VVaidPK_2.py
import simplegui

def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print(count)
    label.set_text(count)


frame = simplegui.create_frame("Manipulating Count", 200, 200)
frame.add_button("Reset", reset)
frame.add_button("Increment", increment)
frame.add_button("Decrement", decrement)
frame.add_button("Print Count", print_count)
label = frame.add_label('')

frame.start()

###################################################
# Testes

# Note that the GLOBAL count is defined inside a function
# Note que a variável GLOBAL count é definida fora da função
'''/reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()'''
####################################################
# Resultados esperados do teste

# 1
# 2
# -2
