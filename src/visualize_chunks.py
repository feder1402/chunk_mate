import streamlit as st

colors = ["blue", "green", "orange", "red", "violet"]

def visualize_chunks(chunks):    
    chunk_colors = [colors[(ndx + 1) % len(colors)] for ndx in range(len(chunks))]
    # text = ''
    with st.container(height=400, border=True):
        ndx = 0
        for chunk in chunks:
            for line in chunk.page_content.split('\n'):
                sanitized_line = line.replace('$', '&#36;') # Escape dollar signs that creates isssues in Markdown
                st.caption(f':{chunk_colors[ndx]}[{sanitized_line}]')
            ndx += 1
