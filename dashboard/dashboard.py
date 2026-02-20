import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

day_df = pd.read_csv(os.path.join(BASE_DIR, "day.csv"))
hour_df = pd.read_csv(os.path.join(BASE_DIR, "hour.csv"))

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

weather_map = {
    1: "Clear",
    2: "Mist",
    3: "Light Snow/Rain",
    4: "Heavy Rain/Snow"
}

season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

day_df['weathersit'] = day_df['weathersit'].map(weather_map)
hour_df['weathersit'] = hour_df['weathersit'].map(weather_map)

day_df['season'] = day_df['season'].map(season_map)
hour_df['season'] = hour_df['season'].map(season_map)

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚴",
    layout="wide"
)

st.title("🚴 Bike Sharing Dashboard")
st.markdown("""
Dashboard ini menampilkan analisis penyewaan sepeda berdasarkan kondisi cuaca dan jam penggunaan selama tahun 2011–2012.
""")

st.sidebar.header("📅 Filter Data")

start_date = st.sidebar.date_input(
    "Tanggal Mulai",
    day_df["dteday"].min()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir",
    day_df["dteday"].max()
)

filtered_day = day_df[
    (day_df["dteday"] >= pd.to_datetime(start_date)) &
    (day_df["dteday"] <= pd.to_datetime(end_date))
]

filtered_hour = hour_df[
    (hour_df["dteday"] >= pd.to_datetime(start_date)) &
    (hour_df["dteday"] <= pd.to_datetime(end_date))
]

st.subheader("📊 Statistik Ringkasan")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(filtered_day["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", int(filtered_day["cnt"].mean()))
col3.metric("Jumlah Hari Data", int(filtered_day.shape[0]))


st.subheader("🌤️ Pengaruh Kondisi Cuaca terhadap Penyewaan")

weather_avg = filtered_day.groupby("weathersit")["cnt"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(data=weather_avg, x="weathersit", y="cnt", palette="Blues_d", ax=ax1)

ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Penyewaan")
ax1.set_title("Rata-rata Penyewaan Sepeda per Kondisi Cuaca")

st.pyplot(fig1)


st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")

hour_avg = filtered_hour.groupby("hr")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(data=hour_avg, x="hr", y="cnt", marker="o", ax=ax2)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_title("Rata-rata Penyewaan Sepeda Tiap Jam")

st.pyplot(fig2)