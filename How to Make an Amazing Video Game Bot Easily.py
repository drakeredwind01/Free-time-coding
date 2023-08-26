import gym
import universe

env = gym.make('flashgames.CoasterRaser-v0')
observation_n = env.reset()

while True:
    action_n = [[('keyEvent','ArrowUp',True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()