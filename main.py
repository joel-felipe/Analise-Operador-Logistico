import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("tratado.csv")

# Create a list of possible values and multiselect menu with them in it.
entregador = data['entregador'].unique()
entregador_SELECTED = st.multiselect('Select countries', entregador)

# Mask to filter dataframe
mask_entregador = data['entregador'].isin(entregador_SELECTED)

data = data[mask_entregador]


st.write(data)


soma = data[['valor']].sum()

st.write(soma)

#st.write(soma.style.format("{:.2}"))

#st.dataframe(soma.style.format(formatter="{:.2f}"