import streamlit as st 
import pandas as pd
#------------------------------------------------------------------------------------
# Definindo o ícone da página
url_flaicon = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/favicon-96x96-1.png"
st.set_page_config(page_title="App Economia Teste", page_icon=url_flaicon, layout="wide", initial_sidebar_state="expanded")
#Imagem de Cabeçalho
url_imagem = "https://ppa.go.gov.br/wp-content/uploads/sites/9/2023/05/Governo_Horizontal_-21093b4c-1920w.webp"
# Define o código HTML para centralizar a imagem
html_code = f"<div style='text-align:center'><img src='{url_imagem}' alt='Imagem da web'></div>"
# Exibe a imagem centralizada sem alterar seu tamanho ou qualidade
st.markdown(html_code, unsafe_allow_html=True)
# Definindo o icone da página, título e layout
#Título da Página
st.title('Nota Técnica de Economia')

# -----------------------------------------------------------------------

# Carrega os dados do Excel
df_lista_orgaos = pd.read_excel('PEDIDO DE CRÉDITO ADICIONAL.xlsx', sheet_name='Lista_Órgãos')

# Extrai as siglas da primeira coluna
siglas = df_lista_orgaos.iloc[:, 0].tolist()

# Cria uma linha no layout do Streamlit
col1, col2 = st.columns([0.3, 1])

# Adiciona a combobox na primeira coluna
with col1:
    sigla_selecionada = st.selectbox('Selecione a Sigla:', siglas)

    # Obtém o nome do órgão correspondente à sigla selecionada
    nome_orgao = df_lista_orgaos[df_lista_orgaos.iloc[:, 0] == sigla_selecionada].iloc[0, 1]

# Adiciona o nome do órgão na segunda coluna
with col2:
    st.write('Nome do órgão:')
    st.markdown(f"###### {nome_orgao}") 

# Adiciona um espaço para separar os elementos
st.write('')

# Cria uma linha no layout do Streamlit
col_responsavel, col_whatsapp = st.columns(2)

# Adiciona um campo de entrada de texto na primeira coluna
with col_responsavel:
    st.text_input("Responsável pelas Informações", placeholder="Nome do responsável")

# Adiciona um campo de entrada de texto na segunda coluna
with col_whatsapp:
    st.text_input("WhatsApp",placeholder="xx xxxxx-xxxx")
    
# VALOR TOTAL DA SUPLEMENTAÇÃO
valor_suplementacao = st.text_input("Valor Total da Suplementação",placeholder="Informe o valor total da suplementação")

# OBJETO
valor_objeto = st.text_area("Objeto",placeholder="Descrição do objeto")

# JUSTIFICATIVA
valor_impactos = st.text_area("Justificativa",placeholder="Impactos do não atendimento do pedido")

# TABELA 1  INDICAÇÃO DAS CLASSIFICAÇÕES ORÇAMENTÁRIAS IMPACTADAS PELA SUPLEMENTAÇÃO
st.markdown(f"##### TABELA 1 : INDICAÇÃO DAS CLASSIFICAÇÕES ORÇAMENTÁRIAS IMPACTADAS PELA SUPLEMENTAÇÃO") 
columns = ["CLASSIFICAÇÃO ORÇAMENTÁRIA","VALOR SUP (+) / RED (-)"]
df_tabela1 = pd.DataFrame(columns=columns)
tabela1 = st.data_editor(df_tabela1, num_rows='dynamic', use_container_width=True)


# TABELA 2 DETALHAMENTO DO PEDIDO DE SUPLEMENTAÇÃO
st.markdown("##### TABELA 2 : DETALHAMENTO DO PEDIDO DE SUPLEMENTAÇÃO") 

columns = ["Nº SOLICIT. SIOFI", "COD. AÇÃO", "AÇÃO", "PRODUTO", "INICIATIVA", 
           "VALOR A SER SUPLEMENTADO", "ORIGEM DO RECURSO", "AÇÃO A SER ANULADA", 
           "VALOR A SER REDUZIDO"]

# Inicializa o dataframe vazio
df_tabela2 = pd.DataFrame(columns=columns)

df_lista_origem = pd.read_excel('PEDIDO DE CRÉDITO ADICIONAL.xlsx', sheet_name='Lista_Origem de Recursos')

# Extrai os dados da primeira coluna
lista_origem = df_lista_origem.iloc[:, 0] 

# Configuração da SelectboxColumn para a coluna "ORIGEM DO RECURSO"
column_config = {
    "ORIGEM DO RECURSO": st.column_config.SelectboxColumn(
        label="Origem do Recurso",
        help="Selecione a origem do recurso",
        width="medium",
        options=lista_origem
    )
}

# Criação do data_editor com as configurações de coluna e a função on_change
tabela2 = st.data_editor(
    df_tabela2,
    column_config=column_config,
    hide_index=True,
    num_rows='dynamic', 
    use_container_width=True
)

# TABELA 3 DETALHAMENTO DO PEDIDO DE SUPLEMENTAÇÃO
st.markdown("##### TABELA 3: ELEMENTOS DO MACROPROCESSO ORÇAMENTÁRIO AFETADOS PELO PEDIDO DE SUPLEMENTAÇÃO") 

columns = ["AÇÃO", "PRODUTO", "META FÍSICA ATUAL", "UNIDADE DE MEDIDA", "ACUMU-LA?", 
           "CUSTO ESTIMADO DO PRODUTO (PPA) PARA O ANO", "CUSTO UNITÁRIO MÉDIO ESTIMADO (PPA) PARA O ANO", 
           "SALDO ORÇAMENTÁRIO AUTORIZADO ATUAL", "SALDO LIQUIDADO ATUAL"]


# Inicializa o dataframe vazio
df_tabela3 = pd.DataFrame(columns=columns)
# Criação do data_editor com as configurações de coluna e a função on_change
tabela3 = st.data_editor(
    df_tabela3,
    hide_index=True,
    num_rows='dynamic', 
    use_container_width=True
)

# TABELA 4 DETALHAMENTO DO PEDIDO DE SUPLEMENTAÇÃO
st.markdown("##### TABELA 4: EFEITOS DO PEDIDO DE SUPLEMENTAÇÃO NOS ELEMENTOS DO MACROPROCESSO ORÇAMENTÁRIO") 

columns = ["AÇÃO", "PRODUTO", "META FÍSICA PROPOSTA", "% ALTERAÇÃO DA META FÍSICA", 
           "CUSTO ESTIMADO DO PRODUTO SUPLEMENTADO", "CUSTO UNITÁRIO MÉDIO ESTIMADO SUPLEMENTADO", 
           "% SUPLEMENTADO X CUSTO ESTIMADO", "% SUPLEMENTADO X SALDO ORÇAMENTÁRIO", 
           "% LIQUIDADO X SALDO ORÇAMENTÁRIO"]



# Inicializa o dataframe vazio
df_tabela4 = pd.DataFrame(columns=columns)
# Criação do data_editor com as configurações de coluna e a função on_change
tabela3 = st.data_editor(
    df_tabela4,
    hide_index=True,
    num_rows='dynamic', 
    use_container_width=True
)

