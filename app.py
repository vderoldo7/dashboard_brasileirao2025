#Esse projeto foi feito apenas para estudo, visando melhorar meu conhecimento em análise de dados com Python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

# 1. Configuração inicial da página
st.set_page_config(page_title="Dashboard Brasileirão 2025", page_icon="img/download.png", layout="wide")

col1, col2 = st.columns([1, 6])

with col1:
    st.image("img/download.png", width=80)

with col2:
    st.title("Dashboard Brasileirão 2025")
st.markdown("Análise interativa do desempenho dos times na última temporada.")

# 2. Carregamento dos dados => @s.cache_data ajuda a carregar os dados apenas uma vez, deixando o código mais leve
@st.cache_data
def load_data():
    try:
        # Tenta ler o arquivo, evitando que a tela quebre se o CSV não estiver na pasta
        return pd.read_csv("brasileirao_2025.csv", sep=";")
    except FileNotFoundError:
        st.error("⚠️ Arquivo 'brasileirao_2025.csv' não encontrado. Verifique o caminho.")
        return pd.DataFrame()

df = load_data()

# 3. Funções do App (Definidas no topo para melhor organização)
@st.dialog("📊 Detalhes do Time")
def mostrar_detalhes(nome_time, dataframe):
    # Busca os dados do time selecionado
    dados_time = dataframe[dataframe["Time"] == nome_time].iloc[0]
    
    st.write(f"### 🏟️ {nome_time}")
    st.subheader(f"⭐ Artilheiro: {dados_time['Artilheiro na Competição']}")
    
    st.divider()
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Vitórias", dados_time["Vitórias"])
    c2.metric("Gols Marcados", dados_time["Gols Marcados"])
    c3.metric("Gols Sofridos", dados_time["Gols Sofridos"])
    
    saldo = dados_time["Gols Marcados"] - dados_time["Gols Sofridos"]
    st.metric("Saldo de Gols", saldo, delta=int(saldo))

    st.info(f"Situação na Tabela: **{dados_time['Recompensa']}**")

# Para a execução se o DataFrame estiver vazio (caso o CSV não tenha carregado)
if df.empty:
    st.stop()

# 4. Barra lateral para filtros interativos
st.sidebar.header("Filtros de Análise")
recompensa_selecionada = st.sidebar.multiselect(
    "Filtre por zona de classificação:",
    options=df["Recompensa"].unique(),
    default=df["Recompensa"].unique()
)

# Trava de segurança: Se o usuário tirar todos os filtros, avisa e para a execução abaixo
if not recompensa_selecionada:
    st.warning("⚠️ Selecione pelo menos uma zona de classificação na barra lateral para visualizar os dados.")
    st.stop()

# Aplica o filtro no dataframe
df_filtrado = df[df["Recompensa"].isin(recompensa_selecionada)]

# 5. Layout principal: Dividindo em colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Tabela Resumida")
    
    event = st.dataframe(
        df_filtrado[["Time", "Vitórias", "Derrotas", "Empates", "Recompensa"]], 
        use_container_width=True, 
        hide_index=True,
        on_select="rerun",         # Atualiza ao clicar
        selection_mode="single-row" # Apenas um time por vez
    )
    
    selecao = event.selection.rows

with col2:
    st.subheader("🎯 Eficiência: Gols Marcados x Sofridos")
    
    fig_scatter = px.scatter(
        df_filtrado, 
        x="Gols Marcados", 
        y="Gols Sofridos", 
        color="Recompensa", 
        hover_name="Time",
        template="plotly_dark"
    )
    
    # Bônus: Linha diagonal indicando Saldo de Gols = 0
    max_gols = max(df_filtrado["Gols Marcados"].max(), df_filtrado["Gols Sofridos"].max())
    fig_scatter.add_shape(
        type="line", line=dict(dash='dash', color="gray", width=1),
        x0=0, y0=0, x1=max_gols, y1=max_gols
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)

# 6. Gráfico de barras na largura total
st.subheader("🏆 Total de Vitórias por Time")
fig_barras = px.bar(
    df_filtrado.sort_values(by="Vitórias", ascending=False),
    x="Time",
    y="Vitórias",
    color="Recompensa",
    text="Vitórias",
    template="plotly_dark"
)
fig_barras.update_traces(textposition='outside')
st.plotly_chart(fig_barras, use_container_width=True)

# 7. Gatilho para abrir o modal de detalhes
if selecao:
    nome_do_time = df_filtrado.iloc[selecao[0]]["Time"]
    mostrar_detalhes(nome_do_time, df_filtrado)
