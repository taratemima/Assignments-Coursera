# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 1000
score = 0
attempts = 0
minutes = 0
seconds = 0
milliseconds = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global minutes
    global seconds
    global milliseconds
    global interval
    milliseconds = int(t)
    seconds = int(milliseconds)/interval
    minutes = int(seconds)/60
    return str(minutes)+":"+str(seconds)+"."+str(milliseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()
    
def reset():
    global minutes
    global seconds
    global milliseconds
    global attempts
    global score
    timer.stop()
    minutes = 0
    seconds = 0
    milliseconds = 0
    attempts = 0
    score = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    pass

def scorer():
    global attempts
    global score
    global minutes
    global seconds
    global milliseconds
    
    if minutes > 0:
        attempts = attempts + 1
    elif minutes > 0 and (seconds == 0 and milliseconds == 0):
        score = score + 1 
        attempts = attempts + 1
        
    return str(score)+"/"+str(attempts)

# define draw handler
def text_draw(canvas):
    global milliseconds
    global score
    global attempts
    
    canvas.draw_text(format(10), [75,99],40, "White")
    canvas.draw_text(scorer(), [99,25], 32, "Green")
#canvas.draw_text(text, point, font_size, font_color)
    
# create frame
frame = simplegui.create_frame("Timer game", 200, 200)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(text_draw)
scorer()

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
