import streamlit as st

with st.container():
    st.markdown("## 👨‍🔬 Conócenos")
    st.markdown("#### 👥 Nuestro equipo de trabajo")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/estudiante2.png", width=200, caption="🧠 Diego")
    with col2:
        st.image("assets/estudiante1.png", width=200, caption="💻 Felipe Castro")
    with col3:
        st.image("assets/estudiante3.png", width=200, caption="🔬 Juan Diego")

st.markdown("---")

st.markdown("### 🎓 Sobre nosotros")

st.write("""
Somos un grupo de estudiantes de último semestre apasionados por la tecnología, la biotecnología y el desarrollo de soluciones innovadoras.  
Nuestro proyecto se centra en la **🍽️ Detección de Alimentos y la Estimación de Proteínas**, utilizando inteligencia artificial para apoyar procesos alimentarios más saludables, informados y eficientes.

🧠 A través del poder del aprendizaje profundo y la visión por computador, hemos desarrollado un sistema capaz de identificar alimentos sólidos en imágenes o video en tiempo real y estimar su contenido proteico con base en datos nutricionales reales.

📸 El modelo está basado en la arquitectura YOLOv11s, entrenado con más de 900 imágenes de alimentos típicos —como lentejas, arroz, carne, yuca o huevos— usando herramientas como Roboflow para el etiquetado y Google Colab para el entrenamiento.

🎯 Este sistema no solo pretende ser una herramienta útil para quienes desean mejorar su dieta, sino que también puede aplicarse en entornos educativos, clínicos o industriales como apoyo al análisis nutricional visual.

Nos enorgullece compartir con ustedes el resultado de meses de dedicación, pruebas y aprendizaje continuo, con la visión de acercar la inteligencia artificial a la vida diaria para transformar la forma en que entendemos lo que comemos.
""")


st.success("💡 ¡Gracias por visitarnos y explorar nuestro proyecto!")

st.markdown("---")

st.markdown("### 📬 Contáctanos")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("📧 Enviar correo", "mailto:felipe@example.com")
with col2:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/felipe-castro-907478182/")
with col3:
    st.link_button("📂 GitHub", "https://github.com/FelipeCastro-js")

st.markdown("---")
st.markdown("🌟 *“Transformando ideas en soluciones, un proyecto a la vez.”*")
st.markdown("📅 Última actualización: Mayo 2025")

