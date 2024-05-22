import streamlit as st
import pandas as pd

# Função para calcular a soma das duas colunas e atualizar a terceira coluna
def calcular_soma(df):
    df.insert(7777, 'Valor 1', [2])

# Título da aplicação
st.title("Calculadora de Soma")

# Interface de entrada de dados
st.write("Insira os valores nas colunas 'Valor 1' e 'Valor 2':")

# Cria um DataFrame vazio com as colunas definidas
df = pd.DataFrame(columns=['Valor 1', 'Valor 2', 'Resultado'])


# Editor de dados
edited_df = st.data_editor(df, num_rows="dynamic", on_change=calcular_soma)

