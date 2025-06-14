import numpy as np
import choix
from typing import List, Tuple


def rankings_to_pairwise(rankings: List[List[int]]) -> List[Tuple[int, int]]:
    pairwise = []
    for ranking in rankings:
        for i in range(len(ranking)):
            for j in range(i + 1, len(ranking)):
                pairwise.append((ranking[i], ranking[j]))
    return pairwise


def fit_plackett_luce(initial_theta: np.ndarray, pairwise_data: List[Tuple[int, int]]) -> np.ndarray:
    n_players = len(initial_theta)
    log_theta_init = np.log(initial_theta)
    estimated_log_theta = choix.ilsr_pairwise(n_players, pairwise_data, alpha=log_theta_init)
    return np.exp(estimated_log_theta)


