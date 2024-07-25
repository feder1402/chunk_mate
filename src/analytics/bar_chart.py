import streamlit as st
import pandas as pd
import altair as alt

def bar_chart(sizes, average):
    st.subheader('Chunk Sizes')
    size_df = pd.DataFrame({'chunk': range(len(sizes)), 'size': sizes})
    bars = alt.Chart(size_df).mark_bar().encode(
        x='chunk',
        y='size'
    )
    highlight = bars.mark_bar(color="#ffffff").encode(
        y2=alt.Y2(datum=average)
    ).transform_filter(
        alt.datum.Value > average
    )
    rule = alt.Chart().mark_rule().encode(
        y=alt.Y(datum=average)
    )
    st.altair_chart(bars + highlight + rule, use_container_width=True, selection_mode='point')