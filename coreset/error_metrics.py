import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min

def relative_error(original_pixels: np.ndarray, coreset_points: np.ndarray) -> float:
    closest_indices, distances = pairwise_distances_argmin_min(original_pixels, coreset_points)
    mse = np.mean(distances ** 2)
    variance = np.var(original_pixels)
    if variance == 0:
        return 0.0
    return mse / variance