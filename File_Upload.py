import streamlit as st
import pandas as pd 
from warnings import filterwarnings
filterwarnings('ignore') 



col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("File_Upload.py", label="File Uploader", icon="🏠")
with col2:    
    st.page_link("pages/Data_Cleaning.py", label="Data Cleaning", icon="🏠")
with col3:
    st.page_link("pages/Feature_Encoding.py", label="Feature Encoding", icon="🏠")
with col4:
    st.page_link("pages/Feature_Scaling.py", label="Feature Scaling", icon="🏠")

st.title('Upload Your File Here')
Data=st.file_uploader('Upload The CSV FILE',type='csv')

st.session_state['Data'] = Data
 

if Data :
    Read = pd.read_csv(Data)
    st.session_state['Read'] = Read 
    if 'Data' in st.session_state and 'Read' in st.session_state:
        Data =st.session_state['Data']
        Read = st.session_state['Read']

        st.subheader('Shape Of Data')
        st.write(Read.shape)

        st.subheader('Data Preview')
        st.dataframe(Read.head())

        st.subheader('Data Type')
        st.dataframe(Read.dtypes)

        st.subheader('Data Describe')
        st.dataframe(Read.describe().T)

        if st.button("Go to Data Cleaning"):
            st.session_state['Read'] = Read 
            st.switch_page('C:/Users/singh/OneDrive/Documents\Projects/Data Processing UI(Streamlit)/pages/Data_Cleaning.py')