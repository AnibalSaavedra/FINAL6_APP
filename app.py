# -*- coding: utf-8 -*-
# SISTEMA UNIFICADO: MBI 360° - RITUAL
# Autor: Aníbal Saavedra

import streamlit as st
from datetime import datetime
from modulo_disociacion import ejecutar_test_disociacion
from modulo_epigenetico import ejecutar_test_epigenetico
from modulo_condiciones import ejecutar_test_condiciones_clinicas
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def guardar_en_sheets(datos_dict):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "inbound-augury-466319-f7-3c6de389e00b.json", scope
    )
    client = gspread.authorize(creds)
    sheet = client.open("MBI360_Respuestas").sheet1
    fila = list(datos_dict.values())
    sheet.append_row(fila)

st.set_page_config(page_title="MBI 360°", page_icon="🌀", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")

st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB
""")

st.markdown("### Selecciona uno o varios módulos que deseas realizar:")

modulos = [
    "Test de disociación o trauma",
    "Estado epigenético emocional (líneas materna/paterna)",
    "Condiciones clínicas opcionales"
]

modulos_seleccionados = st.multiselect("", modulos)

if not modulos_seleccionados:
    st.warning("Selecciona al menos un módulo para continuar.")
else:
    if "Test de disociación o trauma" in modulos_seleccionados:
        ejecutar_test_disociacion()
    if "Estado epigenético emocional (líneas materna/paterna)" in modulos_seleccionados:
        ejecutar_test_epigenetico()
    if "Condiciones clínicas opcionales" in modulos_seleccionados:
        ejecutar_test_condiciones_clinicas()

st.markdown("---")
st.markdown("📲 ¿Necesitas ayuda o una consulta personalizada? [Contáctame por WhatsApp](https://wa.me/56967010107)")

import os

# Mostrar enlaces y botones al finalizar evaluación
st.markdown("---")
st.subheader("📊 Resultados del Test")

# 1. Enlace directo a Google Sheets
st.markdown("🔗 [Ver respuestas en Google Sheets](https://docs.google.com/spreadsheets/d/1YOyK9Ev_bNf7tiHaQuZydNeZ_9vUNqZs4W2zD09rR2U/edit?usp=sharing)")

# 2. Descargar CSV
csv_path = "respuestas_mbi360.csv"
if os.path.exists(csv_path):
    with open(csv_path, "rb") as f:
        st.download_button("📥 Descargar archivo CSV", f, file_name="respuestas_mbi360.csv")
else:
    st.warning("⚠️ El archivo CSV aún no se ha generado.")

# 3. Descargar PDF
pdf_path = "informe_mbi360.pdf"
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        st.download_button("📄 Descargar Informe PDF", f, file_name="informe_mbi360.pdf", mime="application/pdf")
else:
    st.warning("⚠️ El archivo PDF aún no se ha generado.")

# 4. Confirmación WhatsApp
st.success("✅ El mensaje fue enviado correctamente a tu WhatsApp Business: +56 9 6701 0107")
