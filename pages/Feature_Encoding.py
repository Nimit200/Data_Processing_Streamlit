import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("File_Upload.py", label="File Uploader", icon="🏠")
with col2:    
    st.page_link("pages/Data_Cleaning.py", label="Data Cleaning", icon="🏠",disabled=True)
with col3:
    st.page_link("pages/Feature_Encoding.py", label="Feature Encoding", icon="🏠")
with col4:
    st.page_link("pages/Feature_Scaling.py", label="Feature Scaling", icon="🏠")


st.title('Feature Encoding')

if  'Read' in st.session_state:
    Read = st.session_state['Read']
    col = Read.select_dtypes(include='O').columns.tolist()
    st.dataframe(Read.head())
    st.subheader('Unique Values')
    Data_col = st.selectbox('Columns',col)
    if col:
        Unique = st.dataframe(Read[Data_col].unique())
        
    method = st.selectbox('Feature Encoding Method',('Label Encoding','One hot Encoding'))
    if Data_col and method:
        if Data_col and method == 'Label Encoding':
            if st.button('Convert into Label Encoding'):
                Read[Data_col] = LabelEncoder().fit_transform(Read[[Data_col]])
                st.success('Covert Successful')
                st.session_state['Read'] = Read

                Read[Data_col] 
        if col and method == 'One hot Encoding':
            if st.button('Convert into One hot Encoding'):
                one_hot = pd.get_dummies(Read[Data_col],dtype='int')
                Read.reset_index(drop = True) 
                one_hot.reset_index(drop = True)
                Read = pd.concat([Read,one_hot],axis='columns')
                Read.drop(columns=Data_col,inplace=True)
                st.dataframe(Read.head())
                st.session_state['Read'] = Read

if st.button('Go to Feature Scaling'):
    st.session_state['Read'] = Read 
    st.switch_page('C:/Users/singh/OneDrive/Documents/Projects/Data Processing UI(Streamlit)/pages/Feature_Scaling.py')
                 
                 