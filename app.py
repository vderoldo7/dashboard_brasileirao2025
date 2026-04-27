import os
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração inicial da página
st.set_page_config(page_title="Dashboard Brasileirão 2025", page_icon="⚽", layout="wide")
st.title("⚽ Dashboard Brasileirão 2025")
st.markdown("Análise interativa do desempenho dos times na última temporada.")

# 2. Carregamento dos dados com cache para otimizar a performance
@st.cache_data
def load_data():
    # Lê o CSV usando o separador ponto e vírgula, conforme criamos anteriormente
    df = pd.read_csv("brasileirao_2025.csv", sep=";")
    return df

df = load_data()

# 3. Barra lateral para filtros interativos
st.sidebar.header("Filtros de Análise")
recompensa_selecionada = st.sidebar.multiselect(
    "Filtre por zona de classificação:",
    options=df["Recompensa"].unique(),
    default=df["Recompensa"].unique()
)

# Aplica o filtro no dataframe
df_filtrado = df[df["Recompensa"].isin(recompensa_selecionada)]

# 4. Layout principal: Dividindo em colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Tabela Resumida")
    
  
    event = st.dataframe(
        df_filtrado[["Time", "Vitórias", "Derrotas", "Empates", "Recompensa"]], 
        use_container_width=True, 
        hide_index=True,
        on_select="rerun",         # <--- Isso faz o código rodar de novo ao clicar
        selection_mode="single-row" # <--- Permite selecionar apenas um time
    )

  
    selecao = event.selection.rows

with col2:
    st.subheader("🎯 Eficiência: Gols Marcados x Sofridos")
    # Gráfico de dispersão para ver quem ataca bem e defende bem
    fig_scatter = px.scatter(
        df_filtrado, 
        x="Gols Marcados", 
        y="Gols Sofridos", 
        color="Recompensa", 
        hover_name="Time",
        template="plotly_dark" # Tema escuro para combinar com o dashboard
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# 5. Gráfico de barras na largura total
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

# 1. A nova função (Substitua a antiga por esta)
@st.dialog("📊 Detalhes do Time")
def mostrar_detalhes(nome_time):
    dados_time = df[df["Time"] == nome_time].iloc[0]
    
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

# 2. O gatilho que chama a função (Mantenha isso logo abaixo da função)
if selecao:
    nome_do_time = df_filtrado.iloc[selecao[0]]["Time"]
    mostrar_detalhes(nome_do_time)
