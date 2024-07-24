import streamlit as st
import numpy as np

from dotenv import load_dotenv
load_dotenv()

from src.analytics.stats import stats
from src.visualize_chunks import visualize_chunks
from src.text_splitting import get_chunker

SAMPLE_TEXT = \
"""Effective communication is crucial in ensuring that information is easily understood by the reader. One important aspect of clear and concise writing is the practice of breaking up text into smaller, more manageable chunks. By doing so, the reader is able to process the information in a more efficient and organized manner, ultimately enhancing their understanding of the subject matter being presented.
When text is chunked up, it allows for the reader to easily digest the content without feeling overwhelmed. This approach not only improves the overall readability of the material but also ensures that key information is effectively communicated. Furthermore, chunking text helps to maintain the reader's interest and engagement, as they are more likely to stay focused on the content when it is presented in a clear and concise manner.
In summary, the importance of chunking up text should not be underestimated. It is a simple yet effective strategy that can significantly enhance the reader's comprehension and retention of the information being presented. So, the next time you are unsure about how to best convey your message, remember to chunk it out!
Thanks!
"""
st.set_page_config(
    page_title="Chunk Mate",
    page_icon="🧉",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.header('🧉 Chunk Mate', divider=True)

docs = None
method = None
with st.sidebar:
    text_splitter = get_chunker()
  
st.session_state["knowledge"] = st.text_area('Enter or copy your text here', value = SAMPLE_TEXT)
    
if st.session_state["knowledge"]:
    docs = text_splitter.create_documents([st.session_state["knowledge"]])

if docs:
    col = st.columns((1, 5), gap='medium')
    with col[0]:
        st.markdown('### Stats')
        sizes = [len(doc.page_content) for doc in docs]
        average = np.mean(sizes)

        # bar_chart(sizes, average)
        stats(docs, st.session_state["knowledge"], sizes, average)

    with col[1]:
        st.markdown('### Chunks')
        visualize_chunks(docs)
    
