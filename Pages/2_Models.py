import streamlit as st

st.title("ℹ️ Models")
st.write("You can download models from here:")

# List of the filenames qu'ils peuvent télécharger
model_files = ["model_int8.ckpt", "model_fp16.ckpt", "instageo_best_checkpoint-v2.ckpt"]

# Buttons
for model in model_files:
    with open(model, "rb") as file:
        btn = st.download_button(label=f"Download {model}", data=file, file_name=model, mime="application/octet-stream")
