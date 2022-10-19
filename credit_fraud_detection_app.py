import streamlit as st 
import pickle 
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler 
from PIL import Image 
import base64 
st.sidebar.title('Transaction Information')


st.markdown("<h1 style='text-align: center; color: white;'>Credit Fraud Detection</h1>", unsafe_allow_html=True)


model = pickle.load(open('logistic_regression_model', 'rb')) 

V14 = st.sidebar.slider(label="V14-PCA", min_value=-17.50, max_value=2.50, step=0.01) 
V4 = st.sidebar.slider(label="V4-PCA", min_value=-5.00, max_value=12.00, step=0.01) 
V10 = st.sidebar.slider(label="V10-PCA", min_value=-13.50, max_value=4.50, step=0.01) 
V12 = st.sidebar.slider(label="V12-PCA", min_value=-16.50, max_value=2.00, step=0.01) 
V19 = st.sidebar.slider(label="V19-PCA", min_value=-4.00, max_value=5.00, step=0.01) 
V7 = st.sidebar.slider(label="V7-PCA", min_value=-20.50, max_value=6.50, step=0.01) 
V9 = st.sidebar.slider(label="V9-PCA", min_value=-8.50, max_value=3.50, step=0.01) 
V27 = st.sidebar.slider(label="V27-PCA", min_value=-4.00, max_value=2.50, step=0.01) 
V13 = st.sidebar.slider(label="V13-PCA", min_value=-3.50, max_value=3.50, step=0.01)
V11 = st.sidebar.slider(label="V11-PCA", min_value=-3.00, max_value=11.50, step=0.01) 


coll_dict = {'V14-PCA':V14, 'V4-PCA':V4, 'V10-PCA':V10, 'V12-PCA':12, 'V19-PCA':V19, 'V7-PCA':V7, 'V9-PCA':V9, 'V27-PCA':V27, 'V13-PCA':V13, 'V17-PCA':V11}

columns = ['V14','V4','V10','V12','V19','V7','V9','V27','V13','V11']

df_coll = pd.DataFrame.from_dict([coll_dict]) 
user_inputs = df_coll 

prediction = model.predict(user_inputs)




st.markdown("<h2 style='text-align: center; color: white;'>Transaction Information</h2>", unsafe_allow_html=True)

st.table(df_coll)

st.subheader('Click on PREDICT button given below, if configuration is OK')

if st.button('PREDICT'): 
    if prediction[0]==0:
        st.success(prediction[0])
        st.success(f'Transaction is SAFE') 
    elif prediction[0]==1:
        st.warning (prediction[0]) 
        st.warning(f'ALARM! Transaction is FRAUDULENT')
