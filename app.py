import streamlit as st
from math import sqrt

st.set_page_config(page_title="EOQ Calculator", page_icon="📦", layout="centered")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.write("Simulasi sistem persediaan barang untuk menentukan jumlah pemesanan optimal berdasarkan permintaan tahunan, biaya pemesanan, dan biaya penyimpanan.")

# Input Form
with st.form("eoq_form"):
    d = st.number_input("Permintaan Tahunan (unit)", min_value=1.0, step=1.0)
    s = st.number_input("Biaya Pemesanan per Order (Rp)", min_value=0.0, step=100.0)
    h = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=0.0, step=100.0)
    submitted = st.form_submit_button("Hitung EOQ")

if submitted:
    if h == 0:
        st.error("Biaya penyimpanan tidak boleh nol.")
    else:
        eoq = sqrt((2 * d * s) / h)
        total_biaya = (d / eoq) * s + (eoq / 2) * h
        jumlah_pemesanan = d / eoq

        st.header("📈 Hasil Perhitungan")
        st.metric("EOQ (Jumlah Pemesanan Optimal)", f"{eoq:.2f} unit")
        st.metric("Jumlah Pemesanan per Tahun", f"{jumlah_pemesanan:.2f} kali")
        st.metric("Total Biaya Persediaan", f"Rp {total_biaya:,.2f}")
