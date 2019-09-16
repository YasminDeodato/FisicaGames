# Listas
# criado por Yasmin Deodato
# disponível em: http://www.codeskulptor.org/#user46_wwkcQ1JTiQ_6.py
#######################################################################
import simplegui

# Handler for clear button
def clearAll():
    global tasks
    tasks = []
    
# Handler for Task
def newTask(task):
    global tasks
    if(not task in tasks):
        tasks.append(task)

def removeTask(input):
    global tasks
    
    if(len(tasks) > 0):
        if(input.isdigit()):
            input = int(input)
            #if input is a number
            if(input <= len(tasks)):
                #if input is a valid number
                tasks.pop(input-1)
        else:
            #if input is a task
            if(input in tasks):
                tasks.remove(input)
    
# Handler to write on canvas
def draw(canvas):
    global tasks, height, index
    height = 40
    
    for index, item in enumerate(tasks):
        index = str(index + 1) + ": "
        canvas.draw_text(index + item, [20, height], 28, "White")
        height += 30 

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Listas", 500, 400)
task = frame.add_input('Nova tarefa', newTask, 150)
removeTaskNumber = frame.add_input('Remova a tarefa pelo numero', removeTask, 150)
removeTaskName = frame.add_input('Remova a tarefa pelo nome', removeTask, 150)
frame.add_button("Limpar tudo", clearAll)

#reset list
clearAll()
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
