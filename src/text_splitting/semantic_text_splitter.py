import streamlit as st

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

def get_semantic_text_splitter(add_start_index):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large") 
    breakpoint_threshold_type = st.selectbox('Breakpoint threshold type', ['percentile', 'standard_deviation', 'interquartile'])
    return SemanticChunker(
        embeddings, 
        add_start_index=add_start_index, 
        breakpoint_threshold_type=breakpoint_threshold_type
    )
