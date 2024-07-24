import streamlit as st

from langchain_text_splitters import CharacterTextSplitter

from src.common.get_chunk_sizes import get_chunk_sizes

def get_character_text_splitter(add_start_index):

    chunk_size, chunk_overlap = get_chunk_sizes()
    
    with st.expander('Advanced options'):
        separator = st.text_input('Separator', value='')  
        strip_whitespace = st.toggle('Strip whitespace', value=False)            

    return CharacterTextSplitter(
        add_start_index=add_start_index,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=separator, 
        strip_whitespace=strip_whitespace
    )
