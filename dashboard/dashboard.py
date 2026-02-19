import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
day_df = pd.read_csv(os.path.join(BASE_DIR, "day.csv"))
hour_df = pd.read_csv(os.path.join(BASE_DIR, "hour.csv"))


st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚴",
    layout="wide"
)

st.title("🚴 Bike Sharing Dashboard")
st.markdown("""
Dashboard ini menampilkan analisis penyewaan sepeda berdasarkan kondisi cuaca dan jam pemakaian.
""")


st.subheader("📊 Statistik Ringkasan")
col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(day_df["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", int(day_df["cnt"].mean()))
col3.metric("Jumlah Hari Data", int(day_df.shape[0]))


st.subheader("🌤️ Pengaruh Kondisi Cuaca terhadap Penyewaan")

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(x='weathersit', y='cnt', data=day_df, ax=ax1, palette="Blues_d")
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Rata-rata Penyewaan Sepeda per Kondisi Cuaca")
st.pyplot(fig1)


st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(x='hr', y='cnt', data=hour_df, marker="o", ax=ax2)
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Penyewaan")
ax2.set_title("Jumlah Penyewaan Sepeda Tiap Jam")
st.pyplot(fig2)

st.subheader("📅 Filter Penyewaan Berdasarkan Bulan")
month_options = sorted(day_df['mnth'].unique())
selected_month = st.selectbox("Pilih Bulan (1-12)", month_options)

filtered = day_df[day_df['mnth'] == selected_month]

st.markdown(f"### Data Bulan {selected_month}")
st.dataframe(filtered[['dteday', 'weathersit', 'cnt']])