import streamlit as st
def ejecutar_test_epigenetico():
    st.subheader("Módulo 2: Estado Epigenético Emocional")
    st.write("Evalúa tu vínculo con la línea materna y paterna.")
    r1 = st.slider("¿Cómo fue tu relación con tu madre?", 1, 5)
    r2 = st.slider("¿Cómo fue tu relación con tu padre?", 1, 5)
    if st.button("Guardar resultado epigenético"):
        st.success("Datos guardados")
