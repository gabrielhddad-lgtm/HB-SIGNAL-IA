import streamlit as st
import cv2
import numpy as np
from PIL import Image

# -------------------------
# CONFIGURAÇÃO DO APP
# -------------------------
st.set_page_config(
    page_title="HB Signals AI",
    page_icon="📊",
    layout="centered"
)

st.title("📊 HB Signals AI")
st.caption("Análise estatística de gráficos • Timeframe 1M")

# -------------------------
# UPLOAD DA IMAGEM
# -------------------------
uploaded_file = st.file_uploader(
    "📤 Envie a imagem do gráfico",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    st.image(image, use_container_width=True)

    # -------------------------
    # PROCESSAMENTO
    # -------------------------
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    st.subheader("📈 Análise Visual (Bordas)")
    st.image(edges, use_container_width=True, clamp=True)

    st.success("✅ Script Python executado com sucesso")
else:
    st.info("⬆️ Aguardando upload da imagem")

