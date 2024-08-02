import streamlit as st

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

def get_semantic_text_splitter(add_start_index):
    breakpoint_threshold_type = st.selectbox('Breakpoint threshold type', ['percentile', 'standard_deviation', 'interquartile', 'gradient'])
    breakpoint_threshold_amount = st.slider('Breakpoint threshold amount', 0.0, 1.0, 0.8)
   
    embeddings = HuggingFaceEmbeddings()

    return SemanticChunker(
        embeddings, 
        add_start_index=add_start_index, 
        breakpoint_threshold_type=breakpoint_threshold_type,
        breakpoint_threshold_amount=breakpoint_threshold_amount
    )