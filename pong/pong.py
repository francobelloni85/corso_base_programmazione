# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# https://www.youtube.com/watch?v=XGf2GcyHPhc

# TODO
# uscire senza errore >  https://stackoverflow.com/questions/65643645/tkinter-tclerror-invalid-command-name-canvas
# lasciate dentro impostazioni fisse che non si adattano alla grandezza dello schermo
# se lontano dal bordo muovere la pallina senza calcolo traiettoria


import time
import turtle
from threading import Thread
from enum import Enum
from typing import Tuple
import numpy as np


class GameConstants:
    # windows
    WINDOWS_HEIGHT: int = 500
    WINDOWS_WIDTH: int = 800

    # board
    # BOARD_HEIGHT: int = int((WINDOWS_HEIGHT)/2)  # 200
    BOARD_WIDTH: int = int((WINDOWS_WIDTH - 100)/2)    # 350

    BOARD_Y_UPPER_LIMIT = 290
    BOARD_Y_LOWER_LIMIT = -290

    PADDLE_WIDTH: int = 100
    PADDLE_HALF_WIDTH: int = int(PADDLE_WIDTH/2)

    # Ad ogni colpo di quanto aumenta la velocita della pallina
    BALL_SPEED_INCREASE: float = 1.5

    # Di quanto di muove il paddle ad ogni comando
    PADDLE_MOVE: int = 10

    # (-350,+290) ----------------   (+350,+290)
    #     |                               |
    # (-350,0)          (0,0)          (+350,0)
    #     |                               |
    # (-350,-290) ----------------   (+350,-290)


# Informazioni turtle
# le figure di default sono 20px*20px

class Point:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y


class Helper:
    @staticmethod
    def bresenham(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy
        points: list[Point] = []
        while True:
            points.append(Point(x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        return points


class Paddle(Enum):
    A = 1
    B = 2


class PaddleMove(Enum):
    NONE = 0
    UP = 1
    DOWN = 2

# Motore fisico del gioco


class GamePong:

    # Functions

    def paddle_a_up(self):
        y = self.paddle_a.ycor()
        y += GameConstants.PADDLE_MOVE
        if (y + GameConstants.PADDLE_HALF_WIDTH <= GameConstants.BOARD_Y_UPPER_LIMIT):
            self.paddle_a.sety(y)

    def paddle_a_down(self):
        y = self.paddle_a.ycor()
        y -= GameConstants.PADDLE_MOVE
        if (y - GameConstants.PADDLE_HALF_WIDTH >= GameConstants.BOARD_Y_LOWER_LIMIT):
            self.paddle_a.sety(y)

    def paddle_b_up(self):
        y = self.paddle_b.ycor()
        y += GameConstants.PADDLE_MOVE
        if (y + GameConstants.PADDLE_HALF_WIDTH <= GameConstants.BOARD_Y_UPPER_LIMIT):
            self.paddle_b.sety(y)

    def paddle_b_down(self):
        y = self.paddle_b.ycor()
        y -= GameConstants.PADDLE_MOVE
        if (y - GameConstants.PADDLE_HALF_WIDTH >= GameConstants.BOARD_Y_LOWER_LIMIT):
            self.paddle_b.sety(y)

    def set_step_paddle_a(self, step_to_do):
        self.paddle_a_step_to_do = step_to_do

    def set_step_paddle_b(self, step_to_do):
        self.paddle_b_step_to_do = step_to_do

    def get_step_to_do(self, paddle: Paddle):
        if (paddle == Paddle.A):
            return self.paddle_a_step_to_do
        if (paddle == Paddle.B):
            return self.paddle_b_step_to_do
        raise Exception("Devi fornire un valore di paddle corretto")

    def move_paddle_a(self, moves: list[int]):
        move = np.argmax(moves)
        if move == 0:
            return
        if (move == 1):
            self.paddle_a_up()
        else:
            self.paddle_a_down()

    def move_paddle_b(self):
        if self.paddle_b_step_to_do == 0:
            return
        if (self.paddle_b_step_to_do > 0):
            self.paddle_b_up()
            self.paddle_b_step_to_do = self.paddle_b_step_to_do - 1
        else:
            self.paddle_b_down()
            self.paddle_b_step_to_do = self.paddle_b_step_to_do + 1

    def print_score(self):
        self.pen.clear()
        self.pen.write("Player A: {}  Player B: {}".format(
            self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))

    def __init__(self):

        self.score: int = 0
        self.frame_iteration : int = 0

        self.game_info: PlaygroundData = PlaygroundData(self)

        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=GameConstants.WINDOWS_WIDTH, height=GameConstants.WINDOWS_HEIGHT)
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
        # positive height/2 is the top of the screen
        top_height = self.wn.window_height()/2
        # decreasing a little bit so text will be visible
        y = top_height - top_height/50
        self.pen.setposition(0, y)
        self.pen.write("Player A: 0  Player B: 0",
                       align="center", font=("Courier", 24, "normal"))

        # Campo di gioco
        self.board = turtle.Turtle()
        self.board.color("slate gray")
        self.board.speed(0)
        self.board.shape("square")
        self.board.shapesize(stretch_wid=30, stretch_len=35)
        self.board.penup()
        self.board.goto(0, 0)

        # Paddle A
        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        # ovvero 20px x 5 = 100px
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-GameConstants.BOARD_WIDTH, 0)

        # Paddle B
        self.paddle_b = turtle.Turtle()
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(GameConstants.BOARD_WIDTH, 0)

        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 1
        self.ball.dy = 1

        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a_up, "w")
        self.wn.onkeypress(self.paddle_a_down, "s")
        self.wn.onkeypress(self.paddle_b_up, "Up")
        self.wn.onkeypress(self.paddle_b_down, "Down")

        # Step paddle
        self.paddle_a_step_to_do: int = 0
        self.paddle_b_step_to_do: int = 0

        # thread_paddle_a = PaddleThread(Paddle.A, self.set_step_paddle_a, self.game_info)
        # thread_paddle_a.start()

        # thread_paddle_b = PaddleThread(Paddle.B, self.set_step_paddle_b, self.game_info)
        # thread_paddle_b.start()

        self.turn_paddle_a_first: bool = True

    def increase_ball_speed(self):
        pass
        if (abs(self.ball.dx) < 8):
            self.ball.dx = self.ball.dx * GameConstants.BALL_SPEED_INCREASE
            self.ball.dy = self.ball.dy * GameConstants.BALL_SPEED_INCREASE

    def reset_ball_speed(self):
        self.ball.dx = 3
        self.ball.dy = 3

    def reset(self):        
        self.score = 0
        self.frame_iteration = 0
        self.paddle_a.goto(-GameConstants.BOARD_WIDTH, 0)
        self.paddle_b.goto(GameConstants.BOARD_WIDTH, 0)

    def play_step(self, paddle_a_move: list[int] = [0, 0, 0]) -> Tuple[int, bool, int]:
        # -> reward, done, score

        self.wn.update()

        is_game_over: bool = False
        reward: int = 0

        # New ball position
        new_x: int = int(self.ball.xcor() + self.ball.dx)
        new_y: int = int(self.ball.ycor() + self.ball.dy)

        # all the points between the old location and the new one
        all_points: list = Helper.bresenham(
            int(self.ball.xcor()), int(self.ball.ycor()), new_x, new_y)

        # Tolgo il primo punto (che è il punto di partenza)
        points = all_points[1:]

        # Move the paddle
        if (self.turn_paddle_a_first):
            self.move_paddle_a(paddle_a_move)
            self.move_paddle_b()
        else:
            self.move_paddle_b()
            self.move_paddle_a(paddle_a_move)

        self.print_score()

        self.turn_paddle_a_first = not self.turn_paddle_a_first

        # Border checking and collision --------------

        # Per ogni punto della traiettoria controllo se c'è
        # la collisione con il bordo
        # Se si mi porto nella posizione prima del contatto.
        # Se no continuo

        new_position = None

        i: int = 0
        for current_point in points:

            new_position = current_point

            # Top
            if current_point.y >= GameConstants.BOARD_Y_UPPER_LIMIT:
                current_point = all_points[i]
                self.ball.dy *= -1
                break

            # Bottom
            if current_point.y <= GameConstants.BOARD_Y_LOWER_LIMIT:
                current_point = all_points[i]
                self.ball.dy *= -1
                break

            # Check for collision paddle A
            if current_point.x <= -340:
                paddle_upper_limit_a = self.paddle_a.ycor() + 50
                paddle_lower_limit_a = self.paddle_a.ycor() - 50
                if current_point.y < paddle_upper_limit_a and current_point.y > paddle_lower_limit_a:
                    reward = 20
                    current_point = all_points[i]
                    self.ball.dx *= -1
                    self.increase_ball_speed()
                    self.score +=1
                else:
                    reward = -30
                    is_game_over = True                     
                    self.score_a += 1
                    self.print_score()
                    self.reset_ball_speed()
                    self.ball.goto(0, 0)
                    new_position = Point(0, 0)
                    self.ball.dx *= -1
                break

            # Check for collision paddle B
            if current_point.x >= 340:
                paddle_upper_limit_b = self.paddle_b.ycor() + 50
                paddle_lower_limit_b = self.paddle_b.ycor() - 50
                if 1 == 1 or current_point.y < paddle_upper_limit_b and current_point.y > paddle_lower_limit_b:
                    current_point = all_points[i]
                    self.ball.dx *= -1
                    self.increase_ball_speed()
                else:
                    is_game_over = True                    
                    self.score_b += 1
                    self.print_score()
                    self.reset_ball_speed()
                    self.ball.goto(0, 0)
                    new_position = Point(0, 0)
                    self.ball.dx *= -1
                break

            i = i + 1

        # Porto tutti i valori positivi        
        ball_y = self.game_info.get_ball_y() + GameConstants.BOARD_Y_UPPER_LIMIT + GameConstants.PADDLE_HALF_WIDTH 
        paddle_y = self.game_info.get_paddle_y(Paddle.A) + GameConstants.BOARD_Y_UPPER_LIMIT + GameConstants.PADDLE_HALF_WIDTH 
        paddle_top = paddle_y + GameConstants.PADDLE_HALF_WIDTH 
        paddle_bottom = paddle_y - GameConstants.PADDLE_HALF_WIDTH 
        state_3: bool = paddle_bottom <= ball_y <= paddle_top
        if(state_3):
           reward = reward + 1

        # Move the ball
        self.ball.setx(new_position.x)
        self.ball.sety(new_position.y)
                
        return reward, is_game_over, self.score

    def run(self):
        game_score: int = 0
        # Main game loop
        while True:            
            reward, game_over, game_score = self.play_step()            
            if game_over == True:
                break
        print('Final Score', game_score)

# Classe per gestire le informazioni necessarie per muoversi


class PlaygroundData:

    def __init__(self, game: GamePong):
        self.game_info = game

    def get_ball_y(self) -> float:
        return self.game_info.ball.ycor()

    def get_ball_x(self) -> float:
        return self.game_info.ball.xcor()

    def get_step_to_do(self, paddle: Paddle) -> int:
        return self.game_info.get_step_to_do(paddle)

    def get_paddle_y(self, paddle: Paddle) -> float:
        if (paddle == Paddle.A):
            return self.game_info.paddle_a.ycor()
        if (paddle == Paddle.B):
            return self.game_info.paddle_b.ycor()
        raise Exception("Devi fornire un valore di paddle corretto")

    def get_paddle_x(self, paddle: Paddle) -> float:
        if (paddle == Paddle.A):
            return self.game_info.paddle_a.xcor()
        if (paddle == Paddle.B):
            return self.game_info.paddle_b.xcor()
        raise Exception("Devi fornire un valore di paddle corretto")

# Classe dove apportare le modifiche
# Muove il paddle


class PaddleThread (Thread):

    def __init__(self, paddle_name: Paddle, set_step_to_do_paddle, game_info: PlaygroundData):
        Thread.__init__(self)
        self.paddle_name: Paddle = paddle_name
        self.callback_move_paddle = set_step_to_do_paddle
        self.game_info = game_info

    # Qui sviluppare il movimento del paddle
    def run(self):
        if (self.paddle_name == Paddle.A):
            self.run_a()
        else:
            self.run_b()

    # Qui sviluppare il movimento del paddle A
    def run_a(self):
        while True:
            ball_x = self.game_info.get_ball_x()
            ball_y = self.game_info.get_ball_y()
            paddle_x = self.game_info.get_paddle_x(self.paddle_name)
            paddle_y = self.game_info.get_paddle_y(self.paddle_name)
            comand = self.game_info.get_step_to_do(self.paddle_name)
            print("Paddle =" + str(self.paddle_name))
            print("Ball x=" + str(ball_x))
            print("Ball y=" + str(ball_y))
            print("Paddle" + str(self.paddle_name) + " x = " + str(paddle_x))
            print("Paddle" + str(self.paddle_name) + " y = " + str(paddle_y))
            print("Comand = " + str(comand))
            if (comand == 0):
                if (ball_y > paddle_y):
                    self.callback_move_paddle(1)
                else:
                    self.callback_move_paddle(-1)
            # time.sleep(0.01)

    # Qui sviluppare il movimento del paddle B
    def run_b(self):
        while True:
            print("")
            ball_y = self.game_info.get_ball_y()
            paddle_y = self.game_info.get_paddle_y(self.paddle_name)
            if (ball_y > paddle_y):
                self.callback_move_paddle(1)
                print("UP")
            else:
                print("DOWN")
                self.callback_move_paddle(-1)


if __name__ == "__main__":
    main: GamePong = GamePong()
    main.run()
