import streamlit as st
import matplotlib.pyplot as plt

# Perhitungan model M/M/1
def hitung_mm1(lambda_rate, mu_rate):
    if lambda_rate <= 0 or mu_rate <= 0:
        raise ValueError("λ dan μ harus lebih besar dari 0.")
    if lambda_rate >= mu_rate:
        raise ValueError("λ harus lebih kecil dari μ agar sistem stabil (ρ < 1).")

    rho = lambda_rate / mu_rate
    L = lambda_rate / (mu_rate - lambda_rate)
    Lq = (lambda_rate ** 2) / (mu_rate * (mu_rate - lambda_rate))
    W = 1 / (mu_rate - lambda_rate)
    Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))

    return {
        "Utilisasi (ρ)": rho,
        "Jumlah pelanggan dalam sistem (L)": L,
        "Jumlah pelanggan dalam antrian (Lq)": Lq,
        "Waktu dalam sistem (W)": W,
        "Waktu dalam antrian (Wq)": Wq
    }

# Visualisasi diagram batang
def tampilkan_visualisasi(data):
    fig, ax = plt.subplots()
    labels = list(data.keys())
    values = list(data.values())
    
    bars = ax.bar(labels, values, color='teal')
    ax.set_ylabel('Nilai')
    ax.set_title('Visualisasi Hasil Simulasi M/M/1')
    ax.set_xticklabels(labels, rotation=45, ha='right')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, f'{yval:.2f}', ha='center', va='bottom')

    st.pyplot(fig)

# UI Streamlit
st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="centered")
st.title("📟 Aplikasi Simulasi Antrian M/M/1")

st.markdown("Model antrian **M/M/1** digunakan untuk mensimulasikan sistem layanan dengan satu server dan distribusi eksponensial untuk kedatangan dan layanan.")

with st.form("input_form"):
    st.subheader("🔢 Input Parameter:")
    lambda_rate = st.number_input("λ - Rata-rata kedatangan per unit waktu", min_value=0.01, format="%.2f")
    mu_rate = st.number_input("μ - Rata-rata layanan per unit waktu", min_value=0.01, format="%.2f")
    submit = st.form_submit_button("🔍 Hitung")

if submit:
    try:
        hasil = hitung_mm1(lambda_rate, mu_rate)
        st.success("✅ Simulasi berhasil dihitung!")

        st.subheader("📊 Hasil Perhitungan:")
        for nama, nilai in hasil.items():
            st.write(f"**{nama}**: {nilai:.4f}")

        st.subheader("📈 Visualisasi:")
        tampilkan_visualisasi(hasil)

    except ValueError as e:
        st.error(f"❌ {e}")
