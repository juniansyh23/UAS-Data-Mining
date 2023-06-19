import pickle
import streamlit as st

# membaca model
stroke_model = pickle.load(open('stroke_model.sav', 'rb'))

#judul web
st.title('Prediksi Stroke')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    AGE = st.number_input('Input Umur Pasien')
    TENSI = st.number_input('Apakah Tensi Pasien Tinggi? (1 = Ya & 0 = Tidak)')
    JANTUNG = st.number_input('Apakah Pasien Memiliki Riwayat Penyakit Jantung? (1 = Ya & 0 = Tidak)')

with col2 :
    GLUKOSA = st.number_input('Input Kadar Glukosa Pasen')
    BMI = st.number_input('Input Nilai Index Masa Tubuh Pasien')

stroke_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Diagnosis'):
    stroke_prediction = stroke_model.predict([[AGE,TENSI,JANTUNG,GLUKOSA,BMI]])

    if stroke_prediction[0] == 0:
        stroke_diagnosis = 'kemungkinan terkena stroke lebih kecil'
    else:
        stroke_diagnosis = 'kemungkinan terkena stroke lebih besar'
    st.success(stroke_diagnosis)
