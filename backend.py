from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from coreset.image_processing import load_image_from_bytes, extract_pixels
from coreset.coreset_methods import uniform_sampling, weighted_kmeans
from coreset.error_metrics import relative_error
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/compute_coreset/")
async def compute_coreset(file: UploadFile = File(...), method: str = Form(...)):
    img_bytes = await file.read()
    image = load_image_from_bytes(img_bytes)
    pixels = extract_pixels(image)

    sample_size = min(1000, len(pixels))

    if method == "uniform":
        coreset = uniform_sampling(pixels, sample_size)
    elif method == "weighted_kmeans":
        coreset = weighted_kmeans(pixels, sample_size)
    else:
        return JSONResponse(content={"error": "Invalid method"}, status_code=400)

    error = relative_error(pixels, coreset)
    return {"relative_error": error, "coreset_points": coreset.tolist()}
