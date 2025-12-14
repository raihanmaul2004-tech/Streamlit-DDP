import streamlit as st
import csv
import os
from datetime import date


FILE = "rencana.csv"

def tujuan_page():
    st.title("🎯 Tujuan & Rencana Pribadi")

    # --- Baca data lama ---
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)

    # --- Input rencana ---
    tanggal = st.date_input("Pilih Tanggal", value=date.today())
    rencana = st.text_area("Tuliskan Yang Anda Inginkan:")

    if st.button("Simpan Rencana"):
        with open(FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([tanggal, rencana])
        st.success(f"Rencana tanggal {tanggal} tersimpan!")

    # --- Ringkasan sederhana ---
    st.subheader("📄 Ringkasan Rencana")
    if data:
        for row in data:
            if row:
                st.write(f"**{row[0]}** → {row[1]}")