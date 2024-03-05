import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
combined_data = pd.read_csv('combined_data.csv')

# Judul
st.title('Dashboard Streamlit dengan Dataset Combined Data')

# Tampilkan tabel data
st.write('Tabel Data:', combined_data)

# Visualisasi data
st.subheader('Visualisasi Data')


# Scatter plot PM2.5 vs. PM10
st.subheader('Scatter Plot PM2.5 vs. PM10')
fig, ax = plt.subplots()
sns.scatterplot(x='PM2.5', y='PM10', data=combined_data, ax=ax)
st.pyplot(fig)

# Histogram PM2.5
st.subheader('Histogram PM2.5')
fig, ax = plt.subplots()
sns.histplot(combined_data['PM2.5'], ax=ax, bins=20)
st.pyplot(fig)

# Filter
st.sidebar.header('Filter Data')
selected_station = st.sidebar.selectbox('Pilih Station', combined_data['station'].unique())

# Tampilkan data berdasarkan filter
filtered_data = combined_data[combined_data['station'] == selected_station]
st.subheader(f'Data untuk Station {selected_station}')
st.write(filtered_data)


# Ubah kolom 'year', 'month', dan 'day' menjadi format tanggal
combined_data['date'] = pd.to_datetime(combined_data[['year', 'month', 'day']])

# Tetapkan kolom 'date' sebagai index
combined_data.set_index('date', inplace=True)

# Buat Heatmap untuk melihat pola musiman
st.subheader('Heatmap Tingkat Polusi Udara')
fig, ax = plt.subplots(figsize=(10, 8))
heatmap_data = combined_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].resample('M').mean().corr()
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

# Analisis tren menggunakan analisis dekomposisi time series
st.subheader('Analisis Tren Polusi Udara')
for pollutant in ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']:
    st.write(f"Analisis Tren untuk {pollutant}")
    decomposition = seasonal_decompose(combined_data[pollutant], model='additive', period=12)
    fig = decomposition.plot()
    st.pyplot(fig)
    
