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

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(13, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

     # IA
    def get_state(self, game: GamePong):
        
        ball_near_border: int = 25

        data: PlaygroundData = game.game_info

        ball_x = data.get_ball_x()
        ball_y = data.get_ball_y()
        paddle_x = data.get_paddle_x(Paddle.A)
        paddle_y = data.get_paddle_y(Paddle.A)      
        paddle_top = paddle_y + GameConstants.PADDLE_HALF_WIDTH
        paddle_bottom = paddle_y - GameConstants.PADDLE_HALF_WIDTH

        print("Ball x=" + str(ball_x))
        print("Ball y=" + str(ball_y))
        print("Paddle x = " + str(paddle_x))
        print("Paddle y = " + str(paddle_y))
        
        # State
        # 1: 0 > paddle è più vicino al bordo superiore 
        #  : 1 > paddle è più vicino al bordo inferiore        
        # 2: 1 > la pallina è vicina al bordo (entro 25px)
        # 3: 1 > la pallina è al di sopra della dimensione del paddle 
        # 4: 1 > la pallina è al di sotto della dimensione del paddle 
        # 5: 1 > la pallina è dentro la dimensione del paddle 
        # 6: 1 > la pallina è nel campo dell'avversario
        # 7: 1 > la pallina è lontanta 300px
        # 8: 1 > la pallina è lontanta 250px
        # 9: 1 > la pallina è lontanta 200px

        state_1: bool = paddle_y > 0        
        state_2: bool = abs(GameConstants.BOARD_Y_UPPER_LIMIT) - abs(ball_y) < ball_near_border
        state_3: bool = paddle_top < ball_y
        state_4: bool = paddle_bottom > ball_y
        state_5: bool = paddle_bottom < ball_y < paddle_top
        state_6: bool = paddle_x> 0
        
        ball_x_abs: int = abs(ball_x)

        state_7: bool = ball_x < 0  and abs(ball_x) > 300 
        state_8: bool = ball_x < 0  and 250 < ball_x_abs < 300 
        state_9: bool = ball_x < 0  and 200 < ball_x_abs < 250 
        state_10: bool = ball_x < 0 and 150 < ball_x_abs < 200  
        state_11: bool = ball_x < 0 and 100 < ball_x_abs < 150 
        state_12: bool = ball_x < 0 and 50 < ball_x_abs < 100 
        state_13: bool = ball_x < 0 and 25 < ball_x_abs < 50 

        if(int(state_3) + int(state_4) + int(state_5) >1):
            print("mmm")

        if(int(state_7) + int(state_8) + int(state_9) >1):
            print("mmm")

        state = [
            state_1,            
            state_2,
            state_3,
            state_4,
            state_5,
            state_6,
            state_7,
            state_8,
            state_9,
            state_10,
            state_11,
            state_12,
            state_13
            ]
        
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