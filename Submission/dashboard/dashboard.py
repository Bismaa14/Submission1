import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hour_data = pd.read_csv('C:/Users/LENOVO/Documents/Bangkit/projek1/Submission/data/hour.csv')
day_data = pd.read_csv('C:/Users/LENOVO/Documents/Bangkit/projek1/Submission/data/day.csv')

# Judul Dashboard
st.title("Dashboard Analisis Pembagian Sepeda")

# Mengonversi kolom dteday menjadi tipe datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Menghapus kolom 'instant' dari dataset
day_data_cleaned = day_data.drop(columns=['instant'])

# Pertanyaan 1: Hubungan antara Suhu dan Jumlah Penyewaan Sepeda
st.subheader("Korelasi Faktor yang Mempengaruhi Penyewaan Sepeda")
plt.figure(figsize=(12, 6))
corr = day_data_cleaned.corr()  # Menghitung matriks korelasi
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi Heatmap')
st.pyplot(plt)
plt.close()

st.subheader("Visualisasi agar Lebih Dimengerti Pengguna")
# 1. Jenis Penyewa
plt.figure(figsize=(12, 6))
sns.barplot(data=day_data_cleaned, x='registered', y='cnt', ci=None, palette='viridis')
plt.title('Rata-rata Penyewaan Sepeda oleh Penyewa Terdaftar')
plt.xlabel('Jumlah Penyewa Terdaftar')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.legend(['Penyewa Terdaftar'])  # Tambahkan legenda
st.pyplot(plt)
plt.close()

# 2. Hari dalam Minggu
plt.figure(figsize=(12, 6))
sns.barplot(data=day_data_cleaned, x='weekday', y='cnt', ci=None, palette='viridis')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Minggu')
plt.xlabel('Hari dalam Minggu (0 = Minggu, 6 = Sabtu)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])  # Keterangan hari
st.pyplot(plt)
plt.close()

# 3. Waktu dalam Hari
plt.figure(figsize=(12, 6))
sns.barplot(data=hour_data, x='hr', y='cnt', ci=None, palette='viridis')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Jam')
plt.xlabel('Jam (0-23)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
st.pyplot(plt)
plt.close()

# Pertanyaan 2: Pola Penggunaan Sepeda Berdasarkan Musim
st.subheader("Pengaruh Musim Terhadap Penyewaan Sepeda")
plt.figure(figsize=(12, 6))
sns.boxplot(data=day_data_cleaned, x='weathersit', y='cnt')
plt.title('Pengaruh Musim Terhadap Penyewaan Sepeda')
plt.xlabel('Kondisi Musim')
plt.ylabel('Total Sepeda yang Disewakan (cnt)')
plt.xticks([0, 1, 2], ['Buruk', 'Sedang', 'Baik'])  # Keterangan kondisi cuaca
st.pyplot(plt)
plt.close()

st.subheader("Visualisasi agar Lebih Dimengerti Pengguna")
# Tambahkan visualisasi yang lebih mudah dibaca 
plt.figure(figsize=(12, 6))
sns.barplot(data=day_data_cleaned, x='weathersit', y='cnt', estimator=np.mean, ci=None, palette='Set2')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.xticks([0, 1, 2], ['Buruk', 'Sedang', 'Baik'])  # Keterangan kondisi cuaca
st.pyplot(plt)
plt.close()