import streamlit as st
import csv
import os

FILE = "rencana.csv"

def rekap_page():
    st.title("📊 Rekap Tujuan")

    data = []
    if os.path.exists(FILE):
        with open(FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)

    if data:
        st.subheader("Ayo wujudkan keinginanmu!")
        for row in data:
            if row:
                bulan, rencana = row
                st.markdown(
                    f"""
                    <div style="
                        background-color:#1a1a1a;
                        padding:15px;
                        margin-bottom:10px;
                        border-radius:8px;
                        border:1px solid #444;">
                        <h4 style="color:orange; margin:0;">{bulan}</h4>
                        <p style="color:white; margin:0;">{rencana}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.info("Belum ada tujuan yang tersimpan.")