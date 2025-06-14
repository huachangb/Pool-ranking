import numpy as np
from .skill_estimator import SkillEstimator


class LinearSkillEstimator(SkillEstimator):
    def __init__(self, alpha: float = 0.5, beta: float = 0.02):
        self.alpha = alpha
        self.beta = beta

    def __call__(self, features: np.ndarray) -> np.ndarray:
        wins = features[:, 0]
        net_points = features[:, 1] - features[:, 2]
        log_skill = self.alpha * wins + self.beta * net_points
        return np.exp(log_skill)
