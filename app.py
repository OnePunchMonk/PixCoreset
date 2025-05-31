import streamlit as st
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Image Coreset Generator")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
method = st.radio("Select coreset method", options=["uniform", "weighted_kmeans"])

if uploaded_file and method:
    if st.button("Generate Coreset"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {"method": method}

        with st.spinner("Processing..."):
            response = requests.post("http://localhost:8000/compute_coreset/", files=files, data=data)

        if response.status_code == 200:
            result = response.json()
            error = result["relative_error"]
            coreset_points = result["coreset_points"]

            st.success(f"Relative Error: {error:.5f}")

            coreset_np = np.array(coreset_points)
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.scatter(coreset_np[:, 0], coreset_np[:, 1], c=coreset_np / 255, s=5)
            ax.set_title("Coreset Points (scatter plot on RGB channels)")
            ax.set_xlabel("Red Channel")
            ax.set_ylabel("Green Channel")
            st.pyplot(fig)

            df = pd.DataFrame(coreset_points, columns=["R", "G", "B"])
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Coreset CSV",
                data=csv,
                file_name="coreset.csv",
                mime="text/csv"
            )
        else:
            st.error(f"Error: {response.text}")
