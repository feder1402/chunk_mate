import streamlit as st

def get_chunk_sizes():
    chunk_size = st.slider('Chunk Size', min_value=1, max_value=8192, value=35)
    chunk_overlap = st.slider('Overlap Size', min_value=0, max_value=4096, value=4)

    if chunk_overlap >= chunk_size:
        st.warning('Overlap size must be less than chunk size.')
        st.stop()
        
    return chunk_size, chunk_overlap