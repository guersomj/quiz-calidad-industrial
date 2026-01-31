import streamlit as st
import json
import random

# ================= CONFIGURACIÓN DE PÁGINA =================
st.set_page_config(
    page_title="Quiz de Calidad",
    page_icon="✅",
    layout="centered"
)

# ================= ENCABEZADO =================
st.title("🧪 Quiz de Calidad")
st.caption("Proyecto Final · Fundamentos de Programación · Ingeniería Industrial")
st.divider()

# ================= CARGA DE PREGUNTAS =================
with open("preguntas.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

TOTAL_PREGUNTAS_POR_PARTIDA = 4

# ================= ESTADO INICIAL =================
if "preguntas_seleccionadas" not in st.session_state:
    st.session_state.preguntas_seleccionadas = random.sample(
        preguntas, TOTAL_PREGUNTAS_POR_PARTIDA
    )
    st.session_state.puntaje = 0
    st.session_state.pregunta_actual = 0

# ================= QUIZ =================
if st.session_state.pregunta_actual < TOTAL_PREGUNTAS_POR_PARTIDA:
    idx = st.session_state.pregunta_actual
    p = st.session_state.preguntas_seleccionadas[idx]

    # Contador de preguntas
    numero_pregunta = idx + 1
    restantes = TOTAL_PREGUNTAS_POR_PARTIDA - numero_pregunta

    st.markdown(f"### Pregunta {numero_pregunta} de {TOTAL_PREGUNTAS_POR_PARTIDA}")
    st.caption(f"Te quedan {restantes} por responder")

    # Barra de progreso
    st.progress(numero_pregunta / TOTAL_PREGUNTAS_POR_PARTIDA)
    st.divider()

    st.subheader(p["pregunta"])

    opcion = st.radio(
        "Selecciona una opción:",
        p["opciones"],
        key=f"pregunta_{idx}"
    )

    if st.button("Responder"):
        if opcion == p["respuesta"]:
            st.success("✅ Correcto")
            st.session_state.puntaje += 1
        else:
            st.error("❌ Incorrecto")

        st.session_state.pregunta_actual += 1
        st.rerun()

# ================= RESULTADO FINAL =================
else:
    st.divider()
    st.subheader("📊 Resultado final")

    calificacion = (st.session_state.puntaje / TOTAL_PREGUNTAS_POR_PARTIDA) * 10

    st.metric(
        label="Calificación",
        value=f"{calificacion:.1f} / 10",
        delta=f"{st.session_state.puntaje} de {TOTAL_PREGUNTAS_POR_PARTIDA} correctas"
    )

    if st.button("🔄 Reiniciar"):
        st.session_state.clear()
        st.rerun()

# ================= ESTILO SUAVE =================
st.markdown(
    """
    <style>
        .stButton>button {
            border-radius: 10px;
            padding: 0.5em 1.2em;
        }
    </style>
    """,
    unsafe_allow_html=True
)
