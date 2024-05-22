import streamlit as st
import pandas as pd

# Definindo o ícone da página
url_flaicon = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/favicon-96x96-1.png"
#Imagem de Cabeçalho
url_imagem = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/Governo_Horizontal_-21093b4c-1920w.webp"
# Define o código HTML para centralizar a imagem
html_code = f"<div style='text-align:center'><img src='{url_imagem}' alt='Imagem da web'></div>"
# Exibe a imagem centralizada sem alterar seu tamanho ou qualidade
st.set_page_config(page_title="App Economia Teste", page_icon=url_flaicon, layout="wide", initial_sidebar_state="expanded")
st.markdown(html_code, unsafe_allow_html=True)

# Definindo o icone da página, título e layout

#Título da Página
st.title('Nota Técnica de Economia')


# ------------------------------ CABEÇALHO ------------------------------

# numero do processo
numProcesso = st.text_input('Número do Processo', value='', max_chars=None, key=None, type='default', help='Informe o número do processo', placeholder="Informe o número do processo")
# combo box orgaos
numProcesso = st.text_input('Nome', value='', max_chars=None, key=None, type='default', help='Informe o nome ou unidade', placeholder="Informe o nome, unidade ou orgão")
# asssunto
assunto = st.text_input('Assunto', value='', max_chars=None, key=None, type='default', help='Informe o assunto' , placeholder="Informe o assunto")

# ------------------------------ DO ARCABOUÇO NORMATIVO APLICÁVEL ------------------------------
st.markdown("#### 1. DO ARCABOUÇO NORMATIVO APLICÁVEL")
arcabouco = st.text_area('DO ARCABOUÇO NORMATIVO APLICÁVEL', value='', height=None, max_chars=None, key=None)

# ------------------------------ ELABORAÇÃO DO PPA E DA LOA  ------------------------------
st.markdown("#### 2. DA ELABORAÇÃO DO PPA E DA LOA")
elaboracao_ppa_loa = st.text_area('ELABORAÇÃO DO PPA E DA LOA', value='', height=None, max_chars=None, key=None)

# ------------------------------ PLANEJAMENTO DA UNIDADE DEMANDANTE  ------------------------------
st.markdown("#### 3. DO PLANEJAMENTO DA UNIDADE DEMANDANTE")
planejamento_unidade_demandante = st.text_area('PLANEJAMENTO DA UNIDADE DEMANDANTE', value='', height=None, max_chars=None, key=None)


# ------------------------------ ITEM 4  ------------------------------

# DADOS ITEM 4
columns = ["INICIATIVA", "AÇÃO LOA", "ENTREGA", "TIPO DE CRÉDITO ADICIONAL", "VALOR SOLICITADO A TÍTULO DE CRÉDITO ADICIONAL", "JUSTIFICATIVA", "ORIGEM DO RECURSO"]

# Criando o título
st.markdown("#### 4. DA CARACTERIZAÇÃO DO PLEITO")
st.markdown("##### Quadro - Síntese do pleito por crédito adicional")

df_sintese_pleito_credito_adicional = pd.DataFrame(columns=columns)
result_sintese_pleito = st.data_editor(df_sintese_pleito_credito_adicional, num_rows='dynamic' , use_container_width=True )


btn_sintese_pleito = st.button('Ver Tabela')

if btn_sintese_pleito:
    st.write(result_sintese_pleito)
    
# ------------------------------ ITEM 5  ------------------------------
# Definindo as colunas
columns = ["AÇÃO", "ENTREGA", "TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)", 
           "CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)", 
           "CUSTO ESTIMADO ENTREGA DO PPA PARA O QUADRIÊNIO 2024-2027 (c)", 
           "ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)", 
           "RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)", 
           "RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)",
           "RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)", "ALTERAÇÃO DA META"]

# Inicializando o DataFrame vazio no estado da sessão
if 'df_analise_impactos_ppa' not in st.session_state:
    st.session_state.df_analise_impactos_ppa = pd.DataFrame(columns=columns)

# Função para calcular as porcentagens para todas as linhas
def calcular_porcentagens(df):
    df["RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)"] = df["TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)"] / df["CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)"]
    df["RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)"] = df["ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"] / df["CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)"]
    df["RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)"] = df["TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)"] / df["ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"]
    df["ALTERAÇÃO DA META"] = df["RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)"] - df["RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)"]
    return df

# Exibindo o DataFrame
result_analise_cred_add = st.data_editor(st.session_state.df_analise_impactos_ppa, num_rows='dynamic', use_container_width=True)

# Botão para calcular as porcentagens
btn_calcular_porcentagens = st.button("Calcular Porcentagens")

if btn_calcular_porcentagens:
    st.session_state.df_analise_impactos_ppa = calcular_porcentagens(st.session_state.df_analise_impactos_ppa)

btn_analise_cred = st.button('Ver Tabela ')

if btn_analise_cred:
    st.write(st.session_state.df_analise_impactos_ppa)

# ------------------------------ CONCLUSÃO  ------------------------------
st.markdown("### 6. CONCLUSÃO")
conclusao = st.text_area('Conclusão', value='', height=None, max_chars=None, key=None, help='Informe a conclusão')
