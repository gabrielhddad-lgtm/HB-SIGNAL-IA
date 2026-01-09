import streamlit as st
import numpy as np
from PIL import Image, ImageFilter

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
    st.image(image, use_container_width=True)

    # -------------------------
    # ANÁLISE SIMPLES (SEM CV2)
    # -------------------------
    gray = image.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)

    st.subheader("📈 Análise Visual (Bordas)")
    st.image(edges, use_container_width=True)

    st.success("✅ Script Python executado com sucesso")
else:
    st.info("⬆️ Aguardando upload da imagem")
