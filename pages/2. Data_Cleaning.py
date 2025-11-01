import streamlit as st 
import pandas as pd

st.title('Data Cleaning')

if 'Data' in st.session_state and 'Read' in st.session_state:
    Data =st.session_state['Data']
    Read = st.session_state['Read']

    st.subheader('Data Duplicates')
    st.dataframe(Read.head())
    
    st.subheader("Data Duplicates")
    st.write(Read.duplicated().sum())
    if st.button('Remove Duplicates'):
        st.dataframe(Read.drop_duplicated())
        st.write(Read.duplicated().sum())

    st.subheader('Data Null Handling')
    st.write(Read.isnull().sum())
    col = Read.columns.tolist()
    st.selectbox('Columns',(col))
    Method=st.selectbox('Method for Removing Null Values',('Mean','Median','Mode'))
    if     