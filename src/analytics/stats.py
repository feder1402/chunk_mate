import streamlit as st

def stats(docs, knowledge, sizes, average):
    incremental_size=(sum(sizes)/len(knowledge) - 1)*100
    delta = None if int(incremental_size) == 0 else f'{incremental_size:0.0f}%'
    st.metric('Total chunks size', sum(sizes), delta= delta, help='Total number of characters in all chunks')
    st.metric('Chunks', len(docs), help='Number of chunks created')
    st.metric('Min chunk size', min(sizes), help='Smallest chunk size')
    st.metric('Max chunk size', max(sizes), help='Largest chunk size')
    st.metric('Average chunk size', int(average), help='Total chunks size divided by number of chunks')