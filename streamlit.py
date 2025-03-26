import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#Recebe tabelas 
df_review = pd.read_csv("customer reviews.csv")
df_top_100 = pd.read_csv("Top-100 Trending Books.csv")

#Preço Máximo e mínimo de livros 
min_price = df_top_100["book price"].min()
max_price = df_top_100["book price"].max()

#controlador de preço
max = st.sidebar.slider("Price Range", min_price, max_price, max_price)
df_books = df_top_100[df_top_100["book price"] <= max]
df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
st.plotly_chart(fig)
st.plotly_chart(fig2)