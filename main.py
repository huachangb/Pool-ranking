import numpy as np

from ranking_model.ranking.plackett_luce import rankings_to_pairwise, fit_plackett_luce
from ranking_model.skill_estimator import LinearSkillEstimator
from ranking_model.utils import print_rankings


if __name__ == "__main__":
    player_features = np.array([
        [4, 84, 32],
        [4, 84, 60],
        [3, 75, 70],
        [2, 60, 80]
    ])
    rankings = [[0, 1, 2, 3]]

    estimator = LinearSkillEstimator(alpha=0.5, beta=0.02)
    theta = estimator(player_features)
    pairwise = rankings_to_pairwise(rankings)
    estimated_skills = fit_plackett_luce(theta, pairwise)

    print_rankings(estimated_skills)
