# ⚽ Dashboard Brasileirão 2025 📊

# Link do projeto hospedado:

 https://dashboardbrasileirao2025-vitor-deroldo.streamlit.app/

## 📝 Sobre o Projeto
Este projeto é um *Dashboard Interativo* desenvolvido para centralizar e visualizar as estatísticas do Campeonato Brasileiro de 2025.

Através desta ferramenta, é possível:
- Analisar o desempenho dos clubes
- Comparar métricas de ataque e defesa
- Ver a classificação de cada clube
- Comparação de desempenho entre clubes
- Estatística especializada para cada clube

A aplicação transforma dados brutos (CSV) em *insights visuais*, facilitando a compreensão da dinâmica do campeonato.

---

## 🛠️ Tecnologias e Bibliotecas

O projeto foi construído utilizando:

- *Python* → Linguagem principal  
- *Pandas* → Manipulação e tratamento de dados  
- *Plotly* → Gráficos interativos (linhas, barras, pizza, etc.)  
- *Streamlit* → Criação da aplicação web  

---

## 🚀 Como Instalar e Rodar

### 1. Instalar Dependências

Você pode escolher uma das opções abaixo:

🔹 Opção A: Instalação direta
```bash
pip install streamlit pandas plotly
```
🔹 Opção B: Usando requirements.txt (Recomendado)
```bash
pip install -r requirements.txt
```

▶️ Executar a Aplicação

No terminal, dentro da pasta do projeto:

streamlit run app.py
ou
python -m streamlit run app.py
ou
py -m streamlit run app.py

🌐 Acessar no Navegador

O Streamlit abrirá automaticamente.

📁 Estrutura do Projeto
├── data/               # Arquivos de dados (ex: brasileirao_2025.csv)
├── app.py              # Código principal da aplicação
├── requirements.txt    # Lista de dependências
└── README.md           # Documentação do projeto
📌 Funcionalidades
📊 Tabela Geral
Classificação atualizada com base nos dados
📈 Desempenho por Time
Evolução de pontos por rodada
⚔️ Comparativo G4 vs Z4
Análise dos extremos da tabela
🎛️ Estatísticas Interativas
Filtros por:
Rodada
Time
Mandante / Visitante
🧠 Objetivo

Projeto desenvolvido com foco em:

Estudo de análise de dados
Visualização interativa
Aplicações com Streamlit

# Detalhes

  O projeto contém dois tipos de gráficos que podem ser utilizados para análises, e também possui a tabela do campeonato com dados reais.
  Caso o usuário deseje saber sobre um dado de um time específico, basta clicar no time que no próprio projeto irá abrir uma aba contendo os dados unicamente do time.
  O usuário também pode filtrar no campo esquerdo do dashboard as recompensas de cada time no campeonato (Libertadores, Sulamericana, Neutro e Rebaixamento).


👨‍💻 Autor

Vitor Viana Carneiro Deroldo
