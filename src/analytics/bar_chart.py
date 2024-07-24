import streamlit as st
import pandas as pd
import altair as alt

def bar_chart(sizes, average):
    size_df = pd.DataFrame({'chunk': range(len(sizes)), 'size': sizes})
    c = alt.Chart(size_df).mark_bar().encode(
        x='chunk',
        y='size'
    ).properties(width=600, height=400)
    selection = alt.selection_single(
        on='click',
        fields=['chunk']
    )
    bars = c.add_params(selection)
    highlight = bars.mark_bar(color="#e45755").encode(
        y2=alt.Y2(datum=average)
    ).transform_filter(
        alt.datum.Value > average
    )
    rule = alt.Chart().mark_rule().encode(
        y=alt.Y(datum=average)
    )
    st.altair_chart(bars + highlight + rule, use_container_width=True, selection_mode='point')