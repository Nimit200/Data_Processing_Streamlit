import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("File_Upload.py", label="File Uploader", icon="🏠")
with col2:    
    st.page_link("pages/Data_Cleaning.py", label="Data Cleaning", icon="🏠",disabled=True)
with col3:
    st.page_link("pages/Feature_Encoding.py", label="Feature Encoding", icon="🏠")
with col4:
    st.page_link("pages/Feature_Scaling.py", label="Feature Scaling", icon="🏠")


st.title('Outliers Detection')

if  'Read' in st.session_state:
    Read = st.session_state['Read']
    st.dataframe(Read.head())

    col = Read.select_dtypes(exclude='O').columns.tolist()
    Data_col = st.selectbox('Columns',col)


    fig,ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x=Read[Data_col],data=Read,ax=ax)
    plt.title(f'Box Plot of {Data_col}')
    st.pyplot(fig)


    
    fig,ax = plt.subplots(figsize=(6,4))
    sns.histplot(x=Read[Data_col],data=Read,ax=ax,kde=True)
    plt.title(f'Box Plot of {Data_col}')
    st.pyplot(fig)
            
    Data_col_Remove=st.selectbox('Columns',(col),key=col1)

    Method = st.selectbox('Outlier Remove Method',('IQR','Z-Score'))
    if Data_col and Method:#
        if Method =='IQR':
            if st.button('Remove The Outliers Through IQR'):
                Q1 = np.percentile(Read[Data_col_Remove],25)
                Q2 = np.percentile(Read[Data_col_Remove],50)
                Q3 = np.percentile(Read[Data_col_Remove],75)
                Q1_c,Q2_c = st.columns(2)
                Q3_c,IQR_c = st.columns(2)
                Lower,Upper= st.columns(2)
                with Q1_c:
                    st.write(f'Q1(25th) : {Q1}')
                with Q2_c:
                    st.write(f'Q2(Median) : {Q2}')    
                with Q3_c:
                    st.write(f'Q3(75th) : {Q3}')
                IQR = Q3 - Q1
                with IQR_c:
                    st.write(f'IQR : {IQR}')
                Lower_IQR = Q1 - 1.5*IQR
                with Lower:
                    st.write('Lower',Lower_IQR)
                Upper_IQR = Q1 + 1.5*IQR
                with Upper:
                    st.write('Upper',Upper_IQR)
                outliers = Read[(Read[Data_col_Remove] < Lower_IQR) | (Read[Data_col_Remove] > Upper_IQR)]
                st.write('Outliers',outliers)

                



