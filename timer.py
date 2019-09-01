# Timer
# criado por Yasmin Deodato
# disponível em:http://www.codeskulptor.org/#user46_qPCLcXvbL4_5.py
###################################################################
import simplegui
import random

global time, timeStr, isRunning
global attemptsAll, attemptsRight

# Handlers for timer
def timer_handler():
    global time, timeStr
    time += 1
    timeStr = format(time)

def timer_start():
    global isRunning
    isRunning = True
    timer.start()

def timer_stop():
    global time, isRunning, attemptsAll, attemptsRight
    timer.stop()
    if(isRunning):
        if(time%10 == 0):
            attemptsRight +=1
        attemptsAll += 1
    isRunning = False
    
def timer_reset():
    timer.stop()
    global time, timeStr, attemptsRight, attemptsAll, isRunning
    time = 0
    timeStr = "0:00.0"
    attemptsRight = 0
    attemptsAll = 0
    isRunning = False

# Handler to draw on canvas
def draw(canvas):
    global timeStr, attemptsRight, attemptsAll
    canvas.draw_text(timeStr, [200,150], 48, "Red")
    canvas.draw_text("%i/%i" % (attemptsRight, attemptsAll), [450, 30], 30, "White")
    
# Format function
def format(time):
    a = time/600
    b = time/10%60/10
    c = (time/10) % 10
    d = time%10
   
    return "%i:%i%i.%i" % (a, b, c, d)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Timer", 500, 300)
frame.add_button("Comecar", timer_start)
frame.add_button("Parar", timer_stop)
frame.add_button("Reset", timer_reset)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# Reset timer configuration to start the game
timer_reset()

# Start the frame
frame.start()
