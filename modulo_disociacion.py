import streamlit as st
def ejecutar_test_disociacion():
    st.subheader("Módulo 1: Test de Disociación o Trauma")
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad", min_value=1, step=1)
    resultado = st.radio("¿Te sientes desconectado frecuentemente?", [1, 2, 3])
    if st.button("Guardar resultado disociación"):
        st.success("Datos guardados")
