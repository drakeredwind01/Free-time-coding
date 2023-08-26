import gym

import gym
import universe

env = gym.make('flashgames.CoasterRacer-v0')
observation_n = env.reseet()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)


