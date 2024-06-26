import pickle
import streamlit as st

# Memuat model dari file model.pkl
model = pickle.load(open('model.pkl', 'rb'))

# Definisi aplikasi web dengan judul 'Estimasi Harga Mobil Bekas'
st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input BBM Mobil')
engineSize = st.number_input('Input Engine Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi harga mobil bekas dalam Ponds:', predict)
    st.write('Estimasi harga mobil bekas dalam IDR:', predict * 20000)
