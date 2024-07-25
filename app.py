import streamlit as st
import numpy as np

from dotenv import load_dotenv
load_dotenv()

from src.analytics.bar_chart import bar_chart
from src.analytics.stats import stats
from src.visualize_chunks import visualize_chunks
from src.text_splitting import get_chunker

st.set_page_config(
    page_title="Chunk Mate",
    page_icon="🧉",
    layout="wide",
    initial_sidebar_state="expanded")

with open("public/knowledge.txt", 'r') as file:
    content = file.read()

with st.sidebar:
    st.header('🧉 Chunk Mate', divider=True)

docs = None
with st.sidebar:
    text_splitter = get_chunker()
  
st.session_state["knowledge"] = st.text_area('Enter or copy your text here', value = content, height=200)
    
if st.session_state["knowledge"] and text_splitter:
    docs = text_splitter.create_documents([st.session_state["knowledge"]])

if docs:
    sizes = [len(doc.page_content) for doc in docs]
    average = np.mean(sizes)

    with st.sidebar:
        bar_chart(sizes, average)

    col = st.columns((1, 5), gap='medium')
    with col[0]:
        st.markdown('### Stats')
        stats(docs, st.session_state["knowledge"], sizes, average)

    with col[1]:
        st.markdown('### Chunks')
        visualize_chunks(docs)
    
