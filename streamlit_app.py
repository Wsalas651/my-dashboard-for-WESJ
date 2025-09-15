import streamlit as st
import pandas as pd
import altair as alt

st.title('Demo: Streamlit - Sales')

df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'sales': [10, 15, 7, 12, 9, 20]
})

sel = st.selectbox('Select category', ['All'] + df['category'].unique().tolist())
if sel != 'All':
    df = df[df['category'] == sel]

chart = alt.Chart(df).mark_bar().encode(
    x='category',
    y='sales'
)

st.altair_chart(chart, use_container_width=True)
