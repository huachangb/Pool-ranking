import numpy as np


def print_rankings(skills: np.ndarray) -> None:
    ranked = sorted(enumerate(skills), key=lambda x: -x[1])
    print("Final global ranking:")
    for rank, (player_id, skill) in enumerate(ranked, 1):
        print(f"{rank}. Player {player_id} (skill: {skill:.3f})")
