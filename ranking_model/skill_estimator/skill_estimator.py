import numpy as np
from abc import ABC, abstractmethod


class SkillEstimator(ABC):
    @abstractmethod
    def __call__(self, features: np.ndarray) -> np.ndarray:
        """
        Compute skill parameters from player features.

        Parameters
        ----------
        features : np.ndarray
            Player features of shape (num_players, num_features).

        Returns
        -------
        np.ndarray
            Skill parameters.
        """
        pass
