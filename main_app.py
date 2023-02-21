import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# First streamlit webpage

and here is some stuff
""")

df = pd.read_csv('./data.csv')
df

options = st.selectbox('Which option:', 
                       ['Show plotting feature', 
                        'show slider feature'])

if st.checkbox('Show plotting feature:'):
    sample_df = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a', 'b', 'c']
    )

    st.line_chart(sample_df)

x = st.slider('x')
st.write('2 times x is', 2*x)


