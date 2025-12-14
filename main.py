import streamlit as st
from Keuangan import keuangan_page
from statistik_keuangan import finance_stats
from home import home_page
from tujuan import tujuan_page
from rekap import rekap_page
from kontak import kontak_page

custom_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color:#000000;
}
[data-testid="stHeader"] {
    background-color:#1a1a1a;
}
[data-testid="stSidebar"] {
    background-color:#1a1a1a;
}
h1,h3 {
    color: #FFA500 !important;
    font-weight: bold !important;
}
p {
    color: white !important;
}
table {
    background-color: black !important;
    border: 2px solid #CCCCCC !important;
}
th {
    background-color: black    !important;
}
button {
    background-color: #FFA500 !important;
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

menu=st.sidebar.radio("Menu",["Home","Tujuan & Rencana Pribadi","Rekap Tujuan","Catatan Keuangan","Statistik Keuangan","Kontak Kami"])

if menu=="Catatan Keuangan":
    keuangan_page()
elif menu=="Statistik Keuangan":
    finance_stats()
elif menu=="Home":
    home_page()
elif menu=="Tujuan & Rencana Pribadi":
    tujuan_page()
elif menu=="Rekap Tujuan":
    rekap_page()
elif menu=="Kontak Kami":
    kontak_page()