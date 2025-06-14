import numpy as np
from .skill_estimator import SkillEstimator


class LexicographicSkillEstimator(SkillEstimator):
    def __call__(self, features: np.ndarray) -> np.ndarray:
        # silently ignore the other features
        wins = features[:, 0]
        points_scored = features[:, 1]
        points_conceded = features[:, 2]
        skill_score = wins * 1e6 + points_scored * 1e3 - points_conceded
        normalized = (skill_score - skill_score.min()) + 1e-3
        return normalized