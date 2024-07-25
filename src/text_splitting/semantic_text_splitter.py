import streamlit as st

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

def get_semantic_text_splitter(add_start_index):
    breakpoint_threshold_type = st.selectbox('Breakpoint threshold type', ['percentile', 'standard_deviation', 'interquartile'])
   
    embeddings = HuggingFaceEmbeddings()
    return SemanticChunker(
        embeddings, 
        add_start_index=add_start_index, 
        breakpoint_threshold_type=breakpoint_threshold_type
    )
