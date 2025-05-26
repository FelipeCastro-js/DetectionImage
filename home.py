import streamlit as st

# --- PAGE SETUP ---

about_page = st.Page(
    page="views/about_us.py",
    title="About us",
    icon=":material/account_circle:",
    default=True,
)

project_detection = st.Page(
    page="views/detection.py",
    title="Detección de Proteína en Comida",
    icon=":material/fastfood:",
)

# --- NAVIGATION SETUP ---

pg = st.navigation(
    {
        "Info": [about_page],
        "Project": [project_detection],
    }
)

# --- LOGO SETUP ---

st.sidebar.text("Made with ❤️️ by Felipe")

# --- RUN NAVIGATION ---
pg.run()

