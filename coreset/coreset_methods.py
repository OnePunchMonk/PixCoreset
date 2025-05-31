import numpy as np
from sklearn.cluster import KMeans

def uniform_sampling(pixels: np.ndarray, sample_size: int) -> np.ndarray:
    if sample_size >= len(pixels):
        return pixels
    indices = np.random.choice(len(pixels), sample_size, replace=False)
    return pixels[indices]

def weighted_kmeans(pixels: np.ndarray, sample_size: int) -> np.ndarray:
    kmeans = KMeans(n_clusters=sample_size, random_state=42)
    kmeans.fit(pixels)
    return kmeans.cluster_centers_
