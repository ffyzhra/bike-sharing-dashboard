# Bike Sharing Dashboard
Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan kondisi cuaca dan waktu selama periode tahun 2011–2012 menggunakan dataset Bike Sharing.
Dashboard dibangun menggunakan Streamlit dengan fitur interaktif berupa filter rentang tanggal yang mempengaruhi seluruh visualisasi.

## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pip install -r requirements.txt

## Run Streamlit App
streamlit run dashboard/dashboard.py

## Fitur Dashboard
Dashboard ini memiliki beberapa fitur utama:
- Filter rentang tanggal (interaktif)
- Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda
- Visualisasi jumlah penyewaan sepeda berdasarkan jam
- Eksplorasi data periode 2011–2012
Filter yang dipilih akan mempengaruhi seluruh grafik sehingga pengguna dapat melakukan eksplorasi data secara langsung.

## Dependencies
Library yang digunakan dalam project ini:
- pandas
- numpy
- matplotlib
- seaborn
- streamlit==1.19.0
- altair==4.2.0
Semua dependencies dapat diinstall melalui file requirements.txt.
