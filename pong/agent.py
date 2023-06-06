# Credids to:
# Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake
# https://www.youtube.com/watch?v=L8ypSXwyBds&t=2636s

# pip3 install torch torchvision

# BUGS
# Da far tornare 3 valori da play_step() come da esempio

import torch
import random
import numpy as np
from collections import deque
from model import Linear_QNet, QTrainer
from helper import plot
from pong import GameConstants, GamePong, PlaygroundData, Paddle

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

STATE_COL = 20
STATE_ROW = 20
STATE_PADDLE = 3

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        n_state = STATE_COL + STATE_ROW + STATE_ROW + STATE_PADDLE
        self.model = Linear_QNet(n_state, 512, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

     # IA
    def get_state(self, game: GamePong):
        
        data: PlaygroundData = game.game_info

        ball_x = data.get_ball_x() 
        ball_y = data.get_ball_y() 
        # paddle_x = data.get_paddle_x(Paddle.A)
        paddle_y = data.get_paddle_y(Paddle.A)      
        paddle_top = paddle_y + GameConstants.PADDLE_HALF_WIDTH
        paddle_bottom = paddle_y - GameConstants.PADDLE_HALF_WIDTH

        # Porto tutti i valori positivi
        ball_x = ball_x + GameConstants.BOARD_WIDTH
        ball_y = ball_y + GameConstants.BOARD_Y_UPPER_LIMIT
        paddle_y = paddle_y + GameConstants.BOARD_Y_UPPER_LIMIT
        paddle_top = paddle_top + GameConstants.BOARD_Y_UPPER_LIMIT
        paddle_bottom = paddle_bottom + GameConstants.BOARD_Y_UPPER_LIMIT

        if(paddle_y < 0 or ball_x < 0 or ball_y < 0 or paddle_top < 0 or paddle_bottom < 0): 
            print("mmm")

        print("Ball x=" + str(ball_x))
        print("Ball y=" + str(ball_y))
        print("Paddle y = " + str(paddle_y))

        state_1: bool = ball_y > paddle_top
        state_2: bool = paddle_bottom > ball_y
        state_3: bool = paddle_bottom <= ball_y <= paddle_top

        if(int(state_1) +int(state_2) +int(state_3) >1 ):
            print("A")

        state = [
            state_1,            
            state_2,
            state_3,
            ]        
        
        n_col = int(700 / STATE_COL)
        n_row = int(580 / STATE_ROW)

        t1 = int(ball_x / n_col)
        for i in range(STATE_COL):
            if(t1 != i):
                state.append(False)
            else:
                state.append(True)
                print("t1: ",t1)

        t2 = int(ball_y / n_row)
        i = 0
        for i in range(STATE_ROW):
             if(t2 != i):
                state.append(False)
             else:
                state.append(True)
                print("t2: ",t2)
        
        t3 = int(paddle_y / n_row)
        i = 0
        for i in range(STATE_ROW):
             if(t3 != i):
                state.append(False)
             else:
                state.append(True)
                print("t3: ",t3)

        print(t1,t2,t3)
        print(state)

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        #for state, action, reward, nexrt_state, done in mini_sample:
        #    self.trainer.train_step(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = GamePong()
    score = 0 # TODO 
    while True:
        # get old state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()