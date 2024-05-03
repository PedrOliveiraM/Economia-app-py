import streamlit as st
from fpdf import FPDF
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

st.set_page_config(page_title="App Economia Teste")
st.title('ECONOMIA - Fomulário de Solicitação de Crédito Adicional')


orgaos = ['Ministério da Economia', 'Ministério da Saúde', 'Ministério da Educação', 'Ministério da Justiça']

# COMBO BOX
combobox_orgaos = st.selectbox('Selecione o órgão', orgaos,index=None,placeholder="Selecione o órgão")
objeto = st.text_input('Objeto', value='', max_chars=None, key=None, type='default', help='Informe o objeto')
justificativa = st.text_area('Justificativa', value='', height=None, max_chars=None, key=None, help='Informe a justificativa')


# Dados iniciais para a tabela
columns = ["Número", "Dotação Orçamentária", "Ação", "Produto", "Tipo de Crédito", "Valor Requerido", "Origem do Recurso", "Ação a ser Anulada"]
# Criando o DataFrame vazio
df_info_gerais = pd.DataFrame(columns=columns)
st.markdown("### Tabela informações gerais")
tabela_info_gerais = AgGrid(df_info_gerais, editable=True)


button_info_gerais = st.button("Adicionar","btn_info_gerais")
#adicionar uma nova linha em branco
if button_info_gerais:
    #implementar 
    print("")


#---------------------- Tabela Situalção Atual -------------------------------------


# Colunas do DataFrame
columns = ["Número", "Ação", "Produto", "Meta Física PPA", "Unidade", "Acumulativo (S/N)", "Custo Estimado PPA", "Custo Unitário Médio Estimado", "Orçamento Autorizado BO Atual", "Relação Orçamento Autorizado/Custo Estimado"]

# Criando o DataFrame vazio
df_situacao_atual = pd.DataFrame(columns=columns)
st.markdown("### Tabela situacao atual")
tabela_situacao_atual = AgGrid(df_situacao_atual, editable=True)

#adicionar uma nova linha em branco
button_situacao_atual = st.button("Adicionar","btn_situacao_atual")
if button_situacao_atual:
    #implementar 
    print("")


#---------------------- Tabela Situalção Atual -------------------------------------


# Colunas do DataFrame
columns = ["Número", "Ação", "Produto", "Suplementação", "Meta Proposta", "Relação Meta Proposta/Meta Prevista no PPA", "Custo Unitário Médio Após Suplementação", "Relação Suplementação/Orçamento Autorizado"]

# Criando o DataFrame vazio
df_prognostico = pd.DataFrame(columns=columns)
st.markdown("### Tabela prognóstico")
tabela_prognostico = AgGrid(df_prognostico, editable=True)

#adicionar uma nova linha em branco
button_prognostico = st.button("Adicionar","btn_prognostico")
if button_prognostico:
    #implementar 
    print("")
    
impacto_nao_atendimento = st.text_area('Impactos do não atendimento', value='', height=None, max_chars=None, key=None, help='Informe os impactos do não atendimento')
