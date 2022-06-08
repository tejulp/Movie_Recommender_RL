from gym.envs.registration import register
from reco_env import RecoEnv
from utils import import_data_for_env, evaluate


register(
    id=RecoEnv.id,
    entry_point='reco_env:RecoEnv',
    max_episode_steps=1000000,
    nondeterministic=False
)
