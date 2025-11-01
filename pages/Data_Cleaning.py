import streamlit as st 
import pandas as pd

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("File_Upload.py", label="File Uploader", icon="🏠")
with col2:    
    st.page_link("pages/Data_Cleaning.py", label="Data Cleaning", icon="🏠")
with col3:
    st.page_link("pages/Feature_Encoding.py", label="Feature Encoding", icon="🏠")
with col4:
    st.page_link("pages/Feature_Scaling.py", label="Feature Scaling", icon="🏠")


st.title('Data Cleaning')

if  'Read' in st.session_state:
    Read = st.session_state['Read']
    col = Read.columns.tolist()
    
    st.subheader('Data Duplicates')
    st.dataframe(Read.head())
    
    st.subheader("Data Duplicates")
    st.write(Read.duplicated().sum())
    if st.button('Remove Duplicates'):
        st.dataframe(Read.drop_duplicates(inplace=True))
        st.write('After Remove Duplicate',Read.duplicated().sum())
        st.session_state['Read'] = Read


    st.subheader('Data Null - Values Handling')
    st.write(Read.isnull().sum())
    Data_col=st.selectbox('Columns',(col))
    Method=st.selectbox('Method for Removing Null Values',('Mean','Median','Mode'))
     
    if Data_col and Method:
        if Method == 'Mean':
            if st.button('Remove null values through Mean Method'):
                Read[Data_col].fillna(Read[Data_col].mean(),inplace=True)
                st.write(Read.isnull().sum())
                st.session_state['Read'] = Read
        if Method == 'Median':
            if st.button('Remove null values through Median Method'):
                Read[Data_col].fillna(Read[Data_col].median(),inplace=True)
                st.write(Read.isnull().sum())
                st.session_state['Read'] = Read
        if Method == 'Mode':
            if st.button('Remove null values through Mode Method'):
                Read[Data_col].fillna(Read[Data_col].mode()[0],inplace=True)
                st.write(Read.isnull().sum())
                st.session_state['Read'] = Read

st.subheader('Remove Irrelevant Columns')
Data_col_Remove = st.multiselect('Columns',(col),key=col)
if Data_col_Remove:
    if st.button('Remove Columns'):
        Read.drop(columns=(Data_col_Remove),inplace=True)
        st.success('Succefully Remove')
        st.session_state['Read'] = Read

if st.button('Go to Feature Encoding'):
     st.session_state['Read'] = Read    
     st.switch_page('C:/Users/singh/OneDrive/Documents/Projects/Data Processing UI(Streamlit)/pages/Feature_Encoding.py')