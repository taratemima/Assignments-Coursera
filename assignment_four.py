# Implementation of classic arcade game Pong
#special thanks to Moiz Alhindi
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
    
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [(random.randint(60,180))/60, (-(random.randint(120,240))/60)]
    else:
        ball_vel = [(-(random.randint(60,180)/60)), (-(random.randint(120,240))/60)]
           
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
    paddle1_vel, paddle2_vel, score1, score2 = 0, 0, 0, 0
    spawn_ball(RIGHT)

def limit():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
   
    # check for paddle 1
    if paddle1_pos[1] < HALF_PAD_HEIGHT:
       paddle1_pos[1] = HALF_PAD_HEIGHT
       paddle1_vel = 0
    elif paddle1_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
       paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
       paddle1_vel = 0
     
    # check for paddle 2    
    if paddle2_pos[1] < HALF_PAD_HEIGHT:
       paddle2_pos[1] = HALF_PAD_HEIGHT
       paddle2_vel = 0
    elif paddle2_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
       paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
       paddle2_vel = 0
#This idea I got from Alhindi. Honestly, I wanted to do
#a while loop but I got a time out
#perhaps I could have done it as a try/except statement?
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, time
  
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball   
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    #if paddle1_pos[1] OR paddle2_pos is less than HEIGHT
    #or more than HEIGHT - HALF_PAD_HEIGHT
    limit()
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    # draw paddles
    #paddle 1
    pad1top =  [paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT]
    pad1bot =  [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad1top, pad1bot, PAD_WIDTH, "White")
    #paddle2
    pad2top =  [paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT]
    pad2bot =  [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad2top, pad2bot, PAD_WIDTH, "White")
    # determine whether paddle and ball collide    
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS-1):  
        ball_vel[1] = -ball_vel[1]
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        if (pad1top[1] <= ball_pos[1] <= pad1bot[1]):
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            spawn_ball(LEFT)
            score2 += 1
            
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):
        if (pad2top[1] <= ball_pos[1] <= pad2bot[1]):
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            spawn_ball(RIGHT)
            score1 += 1
   
    # draw scores
    canvas.draw_text(str(score2), (450, 50), 36, "White")
    canvas.draw_text(str(score1), (150, 50), 36, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    move = 8
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += move
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += move
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= move
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= move 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    elif(key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()

