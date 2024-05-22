import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Calculadora de Porcentagem", layout="wide")

# Function to calculate percentages for all rows
def calcular_porcentagens2(df):
    # Normalizando os valores, removendo "R$", "." e "," e convertendo para float
    a = df["TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)"].apply(lambda x: float(re.sub(r'[^\d,]', '', str(x)).replace(',', '.')) if pd.notnull(x) else 0)
    b = df["CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)"].apply(lambda x: float(re.sub(r'[^\d,]', '', str(x)).replace(',', '.')) if pd.notnull(x) else 0)
    d = df["ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"].apply(lambda x: float(re.sub(r'[^\d,]', '', str(x)).replace(',', '.')) if pd.notnull(x) else 0)
    
    # Calculando as porcentagens
    df["RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)"] = (a/b)*100
    df["RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)"] = (d/b)*100
    df["RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)"] = (a/d)*100
    return df

# Definindo as colunas
columns = ["AÇÃO", "ENTREGA", "TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)",
           "CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)",
           "CUSTO ESTIMADO ENTREGA DO PPA PARA O QUADRIÊNIO 2024-2027 (c)",
           "ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"]

# Título da aplicação
st.title("Calculadora de Porcentagem")

# Interface de entrada de dados
st.write("Insira os valores nas colunas abaixo e clique em Calcular:")

# Cria um DataFrame vazio com as colunas definidas
df = pd.DataFrame(columns=columns)

# Editor de dados para a tabela principal
tb_main = st.data_editor(df, num_rows="dynamic")

# Botão para calcular porcentagens
if st.button('Calcular'):
    # Calcula as porcentagens
    tb_relacao = calcular_porcentagens2(tb_main)
    
    # Exibe a tabela de porcentagens
    st.write("Tabela de Porcentagens Calculadas:")
    st.write(tb_relacao)

    # Exibe uma mensagem de sucesso
    st.success("Porcentagens calculadas!")

# Exibe a tabela principal
st.write("Tabela Principal:")
st.write(tb_main)

# Concatena a tabela principal com a tabela de porcentagens
df_completa = pd.concat([tb_main, tb_relacao], axis=1)

# Botão para gerar a tabela completa
if st.button('Gerar Tabela Completa'):
    # Exibe a tabela completa
    st.write("Tabela Completa:")
    st.write(df_completa)
