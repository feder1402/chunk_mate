import streamlit as st

from langchain_text_splitters import MarkdownTextSplitter

from src.common.get_chunk_sizes import get_chunk_sizes

def get_markdown_text_splitter(add_start_index):

    chunk_size, chunk_overlap = get_chunk_sizes()
    
    return MarkdownTextSplitter(
        add_start_index=add_start_index,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
