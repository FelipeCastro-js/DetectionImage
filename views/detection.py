import streamlit as st
from PIL import Image
import tempfile
import os
from ultralytics import YOLO
from collections import defaultdict
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

st.title("🥩 Detección de Alimentos y Estimación de Proteína")
st.write("Sube una imagen y el modelo YOLOv11 detectará los alimentos, estimando cuánta proteína consumirás.")

# ---------------------
# Cargar modelo YOLOv11 entrenado
# ---------------------
@st.cache_resource
def load_model():
    return YOLO("../runs/detect/train/weights/best.pt")

model = load_model()

# ---------------------
# Tabla de proteínas por clase
# ---------------------
proteina_estimaciones = {
    "aguacate": 2,
    "arepa": 1.7,
    "arroz": 2.5,
    "arvejas": 9,
    "avena": 5,
    "carne de cerdo": 27,
    "carne de res": 26,
    "frijoles": 9,
    "garbanzos": 9,
    "huevos": 13,
    "lentejas": 9,
    "manzana": 0.3,
    "papa": 2,
    "pasta": 5,
    "pera": 0.4,
    "pescado": 22,
    "platano": 1,
    "pollo": 27,
    "yuca": 1.5,
    "banana": 1.3,
    "orange": 1.6,
    "broccoli": 1.8,
    "carrot": 0.2,
    "pizza": 11,
    "sandwich": 15
}

# ---------------------
# Subida de imagen
# ---------------------
uploaded_file = st.file_uploader("📤 Sube una imagen de comida", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="📷 Imagen subida", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    with st.spinner("🔍 Detectando y estimando proteínas..."):
        results = model(temp_path)[0]

    img_with_boxes = results.plot()
    st.image(img_with_boxes, caption="🧠 Resultado del modelo", use_container_width=True)

    st.subheader("📊 Resultados de predicción")

    conteo_alimentos = defaultdict(int)

    if hasattr(results, "boxes") and results.boxes is not None:
        for i, box in enumerate(results.boxes):
            cls_id = int(box.cls[0])
            cls_name = results.names[cls_id]
            confianza = box.conf[0].item()
            conteo_alimentos[cls_name] += 1

            st.write(f"🔹 {i+1}. **{cls_name}** — Confianza: {confianza:.2f}")

        st.subheader("💪 Estimación total de proteínas")
        total_proteina = 0

        for alimento, cantidad in conteo_alimentos.items():
            proteina_por_unidad = proteina_estimaciones.get(alimento.lower(), 0)
            proteina_total = cantidad * proteina_por_unidad
            total_proteina += proteina_total
            st.write(f"🔸 {alimento}: {cantidad} detecciones × {proteina_por_unidad} g = **{proteina_total} g**")

        st.success(f"🔚 **Proteína total estimada en la imagen: {total_proteina:.2f} g**")

    else:
        st.warning("⚠️ No se detectaron alimentos en la imagen.")

    os.remove(temp_path)
