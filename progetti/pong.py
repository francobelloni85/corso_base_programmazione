# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# https://www.youtube.com/watch?v=XGf2GcyHPhc

# TODO
# uscire senza errore >  https://stackoverflow.com/questions/65643645/tkinter-tclerror-invalid-command-name-canvas
# Lasciate dentro impostazioni fisse che non si adattano alla grandezza dello schermo

import time
import turtle
from threading import Thread
from enum import Enum

# windows 
WINDOWS_HEIGHT: int = 500
WINDOWS_WIDTH: int = 800

# board
BOARD_HEIGHT : int = int((WINDOWS_HEIGHT - 100)/2)  # 200
BOARD_WIDTH : int = int((WINDOWS_WIDTH - 100)/2)    # 350

BOARD_Y_UPPER_LIMIT = 290
BOARD_Y_LOWER_LIMIT = -290

PADDLE_WIDTH: int = 100
PADDLE_HALF_WIDTH: int = int(PADDLE_WIDTH/2)

# Ad ogni colpo di quanto aumenta la velocita della pallina
BALL_SPEED_INCREASE : float = 1.5

# (-350,+290) ----------------   (+350,+290)
#     |                               |
# (-350,0)          (0,0)          (+350,0) 
#     |                               |
# (-350,-290) ----------------   (+350,-290)


# Informazioni turtle
# le figure di default sono 20px*20px

class Paddle(Enum):
    A = 1
    B = 2

#Gioco
class Main: 
    
    # Functions

    def paddle_a_up(self):
        y = self.paddle_a.ycor()
        y += 20
        if(y + PADDLE_HALF_WIDTH< BOARD_Y_UPPER_LIMIT):
            self.paddle_a.sety(y)

    def paddle_a_down(self):
        y = self.paddle_a.ycor()
        y -= 20
        if(y - PADDLE_HALF_WIDTH> BOARD_Y_LOWER_LIMIT):
            self.paddle_a.sety(y)

    def paddle_b_up(self):
        y = self.paddle_b.ycor()
        y += 20
        if(y + PADDLE_HALF_WIDTH< BOARD_Y_UPPER_LIMIT):
            self.paddle_b.sety(y)

    def paddle_b_down(self):
        y = self.paddle_b.ycor()
        y -= 20
        if(y - PADDLE_HALF_WIDTH> BOARD_Y_LOWER_LIMIT):
            self.paddle_b.sety(y)

    def set_step_paddle_a(self,step_to_do):
        self.paddle_a_step_to_do = step_to_do

    def set_step_paddle_b(self,step_to_do):
        self.paddle_b_step_to_do = step_to_do

    def move_paddle_a(self):
        print("sono A -- GO : " + str(self.paddle_a_step_to_do))        
        if self.paddle_a_step_to_do == 0:
            return    
        if(self.paddle_a_step_to_do > 0):
            self.paddle_a_up()
            self.paddle_a_step_to_do = self.paddle_a_step_to_do - 1 
        else:
            self.paddle_a_down()
            self.paddle_a_step_to_do = self.paddle_a_step_to_do + 1 

    def move_paddle_b(self):
        print("sono B -- GO: " + str(self.paddle_a_step_to_do))
        if self.paddle_b_step_to_do == 0:
            return    
        if(self.paddle_b_step_to_do > 0):
            self.paddle_b_up()
            self.paddle_b_step_to_do = self.paddle_b_step_to_do - 1 
        else:
            self.paddle_b_down()
            self.paddle_b_step_to_do = self.paddle_b_step_to_do + 1 

    def print_score(self):
        self.pen.clear()
        self.pen.write("Player A: {}  Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))
        
    def __init__(self):

        self.game_info: PlaygroundData = PlaygroundData(self)

        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=WINDOWS_WIDTH, height=WINDOWS_HEIGHT)
        self.wn.tracer(0)

        # Score
        self.score_a = 0
        self.score_b = 0

        # Pen for score
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("red")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        top_height = self.wn.window_height()/2  # positive height/2 is the top of the screen
        y = top_height - top_height/50          # decreasing a little bit so text will be visible
        self.pen.setposition(0, y)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
        
        # Campo di gioco
        self.board = turtle.Turtle()
        self.board.color("slate gray")
        self.board.speed(0)
        self.board.shape("square")       
        self.board.shapesize(stretch_wid=30,stretch_len=35)
        self.board.penup()        
        self.board.goto(0, 0)

        # Paddle A
        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5,stretch_len=1) # ovvero 20px x 5 = 100px
        self.paddle_a.penup()
        self.paddle_a.goto(-BOARD_WIDTH, 0)

        # Paddle B
        self.paddle_b = turtle.Turtle()
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(BOARD_WIDTH, 0)

        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.5
        self.ball.dy = 0.5

        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a_up, "w")
        self.wn.onkeypress(self.paddle_a_down, "s")
        self.wn.onkeypress(self.paddle_b_up, "Up")
        self.wn.onkeypress(self.paddle_b_down, "Down")

        # Step paddle
        self.paddle_a_step_to_do = 0
        self.paddle_b_step_to_do = 0

        thread_paddle_a = PaddleThread(Paddle.A, self.set_step_paddle_a, self.game_info)
        thread_paddle_a.start()

        self.turn_paddle_a_first : bool = True

    def increase_ball_speed(self):
        self.ball.dx = self.ball.dx * BALL_SPEED_INCREASE
        self.ball.dy = self.ball.dy * BALL_SPEED_INCREASE

    def reset_ball_speed(self):
        self.ball.dx = 1
        self.ball.dy = 1

    def run(self):

        # Main game loop        
        while True:
            self.wn.update()
            
            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            self.print_score()

            # Move the paddle
            if(self.turn_paddle_a_first):
                self.move_paddle_a()
                self.move_paddle_b()
            else:
                self.move_paddle_b()
                self.move_paddle_a()

            self.turn_paddle_a_first = not self.turn_paddle_a_first

            # Border checking and collision --------------

            # Top
            if self.ball.ycor() > BOARD_Y_UPPER_LIMIT:
                self.ball.sety(BOARD_Y_UPPER_LIMIT)
                self.ball.dy *= -1
            # Bottom
            if self.ball.ycor() < BOARD_Y_LOWER_LIMIT:
                self.ball.sety(BOARD_Y_LOWER_LIMIT)
                self.ball.dy *= -1
            # Left (Vince A)
            if self.ball.xcor() > BOARD_WIDTH:
                self.score_a += 1
                self.print_score()
                self.reset_ball_speed()
                self.ball.goto(0, 0)
                self.ball.dx *= -1
            # Right (Vince B)
            if self.ball.xcor() < -BOARD_WIDTH:
                self.score_b += 1
                self.print_score()
                self.reset_ball_speed()
                self.ball.goto(0, 0)
                self.ball.dx *= -1

            # Paddle and ball collisions ---------------

            # (-350,+290) ----------------   (+350,+290)
            #     | |                             | |
            # (-350,0)          (0,0)          (+350,0) 
            #     | |                             | |
            # (-350,-290) ----------------   (+350,-290)

            # Check for collision paddle A
            if self.ball.xcor() < -340:
                paddle_upper_limit_a = self.paddle_a.ycor() + 50
                paddle_lower_limit_a = self.paddle_a.ycor() - 50
                if self.ball.ycor() < paddle_upper_limit_a and self.ball.ycor() > paddle_lower_limit_a:
                    self.ball.dx *= -1 
                    self.increase_ball_speed()
            
            # Check for collision paddle B            
            if self.ball.xcor() > 340:
                paddle_upper_limit_b = self.paddle_b.ycor() + 50
                paddle_lower_limit_b = self.paddle_b.ycor() - 50
                if self.ball.ycor() < paddle_upper_limit_b and self.ball.ycor() > paddle_lower_limit_b:
                    self.ball.dx *= -1
                    self.increase_ball_speed()


# Classe per gestire le informazioni necessarie per muoversi
class PlaygroundData:

    def __init__(self, game: Main):
        self.game_info = game
    
    def get_ball_y(self) -> float:
        return self.game_info.ball.ycor()
    
    def get_ball_x(self) -> float:
        return self.game_info.ball.xcor()
    
    def get_paddle_y(self,paddle:Paddle) -> float:
        if(paddle == Paddle.A):
            return self.game_info.paddle_a.ycor()
        if(paddle == Paddle.B):
            return self.game_info.paddle_b.ycor()
        raise Exception("Devi fornire un valore di paddle corretto")
    
    def get_paddle_x(self,paddle:Paddle) -> float:
        if(paddle == Paddle.A):
            return self.game_info.paddle_a.xcor()
        if(paddle == Paddle.B):
            return self.game_info.paddle_b.xcor()
        raise Exception("Devi fornire un valore di paddle corretto")

# Classe dove apportare le modifiche
class PaddleThread (Thread):

    def __init__(self, paddle_name: Paddle, set_step_to_do_paddle, game_info: PlaygroundData):
        Thread.__init__(self)
        self.paddle_name: Paddle = paddle_name
        self.callback_move_paddle = set_step_to_do_paddle
        self.game_info = game_info
        
    # Qui sviluppare il movimento del paddle
    def run(self):
        i: int = 0
        while True:
            ball_x = self.game_info.get_ball_x()
            ball_y = self.game_info.get_ball_y()
            paddle_x = self.game_info.get_paddle_x(self.paddle_name)
            paddle_y = self.game_info.get_paddle_y(self.paddle_name)
            print("Ball x=" + str(ball_x))
            print("Ball y=" + str(ball_y))
            print("Paddle" + str(self.paddle_name) + " x = " + str(paddle_x))
            print("Paddle" + str(self.paddle_name) + " y = " + str(paddle_y))

            if (i % 2 == 0):
                print("GO UP")
                self.callback_move_paddle(1)
            else:
                print("GO DOWN")
                self.callback_move_paddle(-1)

            i = i + 1

if __name__ == "__main__":
    main: Main = Main()
    main.run()


