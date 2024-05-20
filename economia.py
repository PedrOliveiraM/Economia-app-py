import streamlit as st
from fpdf import FPDF
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# AREA DE INFOS
orgaos = ['Secretaria da Economia', 'Secretaria da Saúde', 'Secretaria da Educação', 'Secretaria da Justiça']


url_flaicon = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/favicon-96x96-1.png"
st.set_page_config(page_title="App Economia Teste", page_icon=url_flaicon, layout="wide", initial_sidebar_state="expanded")
#Imagem de Cabeçalho
url_imagem = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/Governo_Horizontal_-21093b4c-1920w.webp"
# Define o código HTML para centralizar a imagem
html_code = f"<div style='text-align:center'><img src='{url_imagem}' alt='Imagem da web'></div>"
# Exibe a imagem centralizada sem alterar seu tamanho ou qualidade
st.markdown(html_code, unsafe_allow_html=True)


#Título da Página
st.title('Fomulário de Solicitação de Crédito Adicional')



# COMBO BOX

# numero do processo
numProcesso = st.text_input('Número do Processo', value='', max_chars=None, key=None, type='default', help='Informe o número do processo', placeholder="Informe o número do processo")
# combo box orgaos
combobox_orgaos = st.selectbox('Selecione o órgão', orgaos,index=None,placeholder="Selecione o órgão")
# asssunto
assunto = st.text_input('Assunto', value='', max_chars=None, key=None, type='default', help='Informe o assunto' , placeholder="Informe o assunto")
justificativa = st.text_area('Justificativa', value='', height=None, max_chars=None, key=None, help='Informe a justificativa')


# DADOS ITEM 4
columns = ["INICIATIVA", "AÇÃO LOA", "ENTREGA", "PRODUTO", "TIPO DE CRÉDITO ADICIONAL", "VALOR SOLICITADO A TÍTULO DE CRÉDITO ADICIONAL", "JUSTIFICATIVA", "ORIGEM DO RECURSO"]

# Criando o título
st.markdown("### Quadro - Síntese do pleito por crédito adicional")

df_sintese_pleito_credito_adicional = pd.DataFrame(columns=columns)
tipo_de_credito = ['Suplementar', 'Especial', 'Extraordinário']
config = {
    'TIPO DE CRÉDITO ADICIONAL' : st.column_config.SelectboxColumn('TIPO DE CRÉDITO ADICIONAL', options=tipo_de_credito),
    'VALOR SOLICITADO A TÍTULO DE CRÉDITO ADICIONAL': st.column_config.NumberColumn(
            format="R$%.2f",
        )
}
result_sintese_pleito = st.data_editor(df_sintese_pleito_credito_adicional, num_rows='dynamic' ,column_config = config, use_container_width=True )


btn_sintese_pleito = st.button('Ver Tabela')

if btn_sintese_pleito:
    st.write(result_sintese_pleito)
    
    


# tabela 2
# DADOS ITEM 5
columns = ["AÇÃO", "ENTREGA", "TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)", "CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)", 
           "CUSTO ESTIMADO ENTREGA DO PPA PARA O QUADRIÊNIO 2024-2027 (c)", "ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)", 
           "RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)", "RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)",
           "RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)", "ALTERAÇÃO DA META"]

# Criando o título
st.markdown("### Tabela - Análise dos impactos no PPA 2024-2027 da adição dos créditos")

df_analise_impactos_ppa = pd.DataFrame(columns=columns)
config = {
    'TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)': st.column_config.NumberColumn(
        format="R$%.2f",
    ),
    'CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)': st.column_config.NumberColumn(
        format="R$%.2f",
    ),
    'CUSTO ESTIMADO ENTREGA DO PPA PARA O QUADRIÊNIO 2024-2027 (c)': st.column_config.NumberColumn(
        format="R$%.2f",
    ),
    'ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)': st.column_config.NumberColumn(
        format="R$%.2f",
    ),
    'RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)': st.column_config.NumberColumn(
        format="%.2f%%",
    ),
    'RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)': st.column_config.NumberColumn(
        format="%.2f%%",
    ),
    'RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)': st.column_config.NumberColumn(
        format="%.2f%%",
    ),
}

# Adicionando dados específicos fornecidos
df_analise_impactos_ppa.loc[0] = ["Ação 1", "Entrega 1", 16047633.04, 291315620.00, 1284533197.84, 110536000.00, None, None, None, None]

# Função para calcular as porcentagens para todas as linhas
def calcular_porcentagens(df):
    for index, row in df.iterrows():
        df.at[index, "RELAÇÃO COM O CUSTO ESTIMADO PARA 2024 (a/b)"] = row["TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)"] / row["CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)"] * 100
        df.at[index, "RELAÇÃO COM O CUSTO ESTIMADO (AUTORIZADO 2024/PPA 2024) (d/b)"] = row["ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"] / row["CUSTO ESTIMADO ENTREGA DO PPA PARA O ANO DE 2024 (b)"] * 100
        df.at[index, "RELAÇÃO SUPLEMENTAÇÃO NA LOA (a/d)"] = row["TOTAL DA SUPLEMENTAÇÃO POR PRODUTO (a)"] / row["ORCAMENTO DA AÇÃO AUTORIZADA 2024 (d)"] * 100
    return df

# Exibindo o DataFrame
result_analise_cred_add = st.data_editor(df_analise_impactos_ppa, num_rows='dynamic', column_config=config, use_container_width=True)

# Botão para calcular as porcentagens
btn_calcular_porcentagens = st.button("Calcular Porcentagens")

if btn_calcular_porcentagens:
    df_analise_impactos_ppa = calcular_porcentagens(df_analise_impactos_ppa)


btn_analise_cred = st.button('Ver Tabela ')

if btn_analise_cred:
    st.write(result_analise_cred_add)
