import simplegui

def get_input(input_text):
    print(input_text)
    label.set_text(input_text)


frame = simplegui.create_frame("Echo input", 200, 200)
inp = frame.add_input('Write something', get_input, 100)
label = frame.add_label('')

frame.start()

###################################################
# Testes
'''/
get_input("First test input")
get_input("Second test input")
get_input("Third test input")'''

###################################################
# Saída esperada dos testes

# First test input
# Second test input
# Third test input
