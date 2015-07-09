# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

# define global variables
interval = 100
#1000 * 0.10 seconds
milliseconds = 0
seconds = 0
attempts = 0
player_score = 0
stopwatch = False 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def less_than_ten_print(number):
    if number < 10:
        return "0"+str(number)
    else:
        return str(number)
    
def format(t):
    #we are assuming that the value passed into format is
    #milliseconds
    global minutes
    global seconds
    milliseconds = 0
    minutes = (t/10)/60
    seconds = (t/10)%60
    milliseconds = t%10
    print_mill = less_than_ten_print(milliseconds)
    print_sec = less_than_ten_print(seconds)
    print_min = less_than_ten_print(minutes)
        
    return print_min+":"+print_sec+'.'+print_mill
    #return str(minutes)+':'+str(seconds)+'.'+str(milliseconds)

def scorer():
    #global attempts
    global player_score
    global stopwatch
    global seconds
    #attempts = 0
    #if stopwatch is true
    #increment attempts
    #if stopwatch is true and seconds is equal to zero
    #increment player_score
    #now why does it increment more than one here?
    #if I do a local variable, it only increments once, 
    #and does not do it when I start again
    
    if stopwatch == True:
        attempts = attempts + 1
        #if seconds == 0:
         #   player_score = player_score + 1
            
        
            
    return str(player_score)+"/"+str(attempts)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global stopwatch
    timer.stop()
    stopwatch = True
    
def reset():
    global milliseconds
    global stopwatch
    global attempts
    global player_score 
    timer.stop()
    stopwatch = False
    milliseconds = 0
    attempts = 0
    player_score = 0
    timer.start()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global milliseconds
    milliseconds = milliseconds + 1
    #print milliseconds 

#define draw handler
def text_draw(canvas):
    global milliseconds
    canvas.draw_text(format(milliseconds), [100,100], 25, "White")
    canvas.draw_text(scorer(), [150,50], 25, "Green")
    
# create frame
frame = simplegui.create_frame("Timer game", 200, 200)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(text_draw)

#start frame
frame.start()
timer.start()
