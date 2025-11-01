import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,RobustScaler,StandardScaler

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("File_Upload.py", label="File Uploader", icon="🏠")
with col2:    
    st.page_link("pages/Data_Cleaning.py", label="Data Cleaning", icon="🏠",disabled=True)
with col3:
    st.page_link("pages/Feature_Encoding.py", label="Feature Encoding", icon="🏠")
with col4:
    st.page_link("pages/Feature_Scaling.py", label="Feature Scaling", icon="🏠")


st.title('Feature Scaling')

if  'Read' in st.session_state:
    Read = st.session_state['Read']
    st.dataframe(Read)

    col = Read.select_dtypes(exclude='O').columns.tolist()
    Data_col= st.selectbox('Columns',col)
    Method = st.selectbox('Columns',('Standard Scaler','Min Max Scaler','Robust Scaler'))
    if Data_col and Method:
        if Method == 'Standard Scaler':
            if st.button('Standard Scaler'):
                Read[Data_col] = StandardScaler().fit_transform(Read[col])
                st.dataframe(Read.head())
                st.session_state['Read'] = Read

        if Method == 'Min Max Scaler': 
            if st.button('Min Max Scaler'):
                Read[Data_col] = MinMaxScaler().fit_transform(Read[col])
                st.dataframe(Read.head())
                st.session_state['Read'] = Read

        if Method == 'Robust Scaler':
            if st.button('Robust Scaler'):
                Read[Data_col] = RobustScaler().fit_transform(Read[col])
                st.dataframe(Read.head())
                st.session_state['Read'] = Read
                


Download_CSV=Read.to_csv()
st.download_button(label='Download CSV',data=Download_CSV,mime="text/csv",icon=":material/download:")
if st.button('Go to Outliers '):
    st.switch_page('pages/Outliers.py')