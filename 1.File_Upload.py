import streamlit as st
import pandas as pd 

st.title('Upload Your File Here')
Data=st.file_uploader('Upload The CSV FILE',type='csv')

Read = pd.read_csv(Data)

st.subheader('Shape Of Data')
st.write(Read.shape)

st.subheader('Data Preview')
st.dataframe(Read.head())

st.subheader('Data Type')
st.dataframe(Read.dtypes)

st.subheader('Data Describe')
st.dataframe(Read.describe().T)

if st.button("Go to Data Cleaning"):
    st.session_state['Data'] = Data
    st.session_state['Read'] = Read 

    st.switch_page('C:/Users/singh/OneDrive/Documents/Projects/Unique/pages/2. Data_Cleaning.py')