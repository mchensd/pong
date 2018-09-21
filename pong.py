import time
import os
import turtle
import random
wn = turtle.Screen()


wn.addshape('pong/rect1.gif')
player = turtle.Turtle()
player.penup()
player.shape('pong/rect1.gif')
player.speed(0)
player.goto(-300,0)


player2=turtle.Turtle()
player2.penup()
player2.shape('pong/rect1.gif')
player2.speed(0)
player2.goto(300,0)


ball=turtle.Turtle()
ball.penup()
ball.shape('circle')



global t_dir, t2_dir
t_dir = [0,0]  # direction of player
t2_dir = [0,0] # direction of player2


def print_pos(x, y):
    print(x, y)

def up():
    global t2_dir
    t2_dir=[0,4]

def s():
    global t_dir
    t_dir = [0,-4]

def w():
    global t_dir
    t_dir=[0,4]

def down():
    global t2_dir
    t2_dir = [0,-4]



turtle.listen()
def unbind():
    turtle.onkey(None, 'Up')
    turtle.onkey(None, 'Down')
    turtle.onkey(None, 'w')
    turtle.onkey(None, 's')

def bind():
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(w, 'w')
    turtle.onkey(s, 's')

bind()
# wn.onclick(print_pos) # for debugging
player.penup()
ball_dir = [4*random.choice([-1,1]), random.choice([-1,1])*2]


turtle.tracer(0,0)
# https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end

inc = 0
# this is added to the upper bound of the random range every time the ball bounces
# to make the ball bounce more random and fast as the round goes on


time.sleep(1)
s1=0
s2=0
while True:
    players = [player, player2]
    dirs = [t_dir, t2_dir]
    for i in range(2):
        if players[i].ycor() + 90 >= 297 and dirs[i][1] > 0 or players[i].ycor() - 90 <= -291 and dirs[i][1] < 0:
            dirs[i][1] = 0
    player.goto(player.pos()+t_dir)
    player2.goto(player2.pos()+t2_dir)
    ball.goto(ball.pos() + ball_dir)



    if -260 < ball.xcor() < -255.0 and player.ycor()-90 < ball.ycor() < player.ycor() + 90 or 255 < ball.xcor() < 260 and \
            player2.ycor() - 90 < ball.ycor() < player2.ycor() + 90:
        # if ball hit paddle

        inc += .2
        ball_dir[0] = -1*ball_dir[0]
        sign = (ball_dir[1] > 0) - (ball_dir[1] < 0)
        vals = (sign * (2), sign * (inc + 4))
        ball_dir[1] = random.uniform(min(vals), max(vals))

    if ball.ycor() < -290 or ball.ycor() > 300:
        # if ball hit wall

        inc += .2
        ball_dir[1] = -1 * ball_dir[1]
        sign = (ball_dir[1] > 0) - (ball_dir[1] < 0)
        vals = (sign * (2), sign * (inc + 4))
        ball_dir[1] = random.uniform(min(vals), max(vals))

    if ball.xcor() < -350 or ball.xcor() > 350:
        # if ball goes out

        unbind() # don't let user input anything while resetting ... doesn't work

        if ball.xcor() < -350:
            s2 += 1
            print("Player 2 Won!")
        else:
            s1+=1
            print("Player 1 Won!")
        print("Score: {} {}".format(s1,s2))

        ball.goto(0,0)
        ball_dir = [random.choice([-1,1])*4, random.choice([-1,1])*2]

        inc=0

        t_dir = [0,0]
        t2_dir=[0,0]

        player.goto(-300, 0)
        player2.goto(300, 0)

        turtle.update()
        time.sleep(1)
        bind()

    turtle.update() # don't update until everything has moved

wn.mainloop()