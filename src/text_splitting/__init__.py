import streamlit as st

from src.text_splitting.character_text_splitter import get_character_text_splitter
from src.text_splitting.recursive_character_text_splitter import get_recursive_character_text_splitter
from src.text_splitting.semantic_text_splitter import get_semantic_text_splitter
from src.text_splitting.markdown_text_splitter import get_markdown_text_splitter

def get_chunker():
    with st.container(border=True):
        split_method = None
        with st.sidebar:
            split_method = st.selectbox('Split method', ['Character', 'Recursive Character', 'Markdown', 'Semantic'], index=1)
            if split_method == 'Character':
                return get_character_text_splitter(add_start_index=True)
            elif split_method == 'Markdown':
                return get_markdown_text_splitter(add_start_index=True)
            elif split_method == 'Recursive Character':
                return get_recursive_character_text_splitter(add_start_index=True)
            elif split_method == 'Semantic':
                return get_semantic_text_splitter(add_start_index=True)
            else:
                raise ValueError(f'Chunker {split_method} not supported')
