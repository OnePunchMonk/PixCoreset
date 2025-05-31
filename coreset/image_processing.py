from PIL import Image
import numpy as np
from io import BytesIO

def load_image_from_bytes(img_bytes: bytes) -> Image.Image:
    image = Image.open(BytesIO(img_bytes)).convert("RGB")
    return image

def extract_pixels(image: Image.Image) -> np.ndarray:
    arr = np.array(image)
    pixels = arr.reshape(-1, 3)
    return pixels
