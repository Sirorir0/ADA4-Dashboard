import calendar
import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit run "C:\Users\HP OMEN\PycharmProjects\PracticaStreamlit\Dashboard_Cafe.py"

st.header("Afluencia de clientes cafe internet")

dfCafe = pd.read_excel("resultadoLimpieza.xlsx")

#sideBar para controles
#borrar del calendar la primera []

anios = list(set(dfCafe["fechaEntrada"].dt.year))
mes = list(set(dfCafe["fechaEntrada"].dt.month_name())) #ordenar los meses
calendario = list(calendar.month_name)
del calendario [0]

mes_sorted = calendario

st.sidebar.title("Filtros")

anioSelec = st.sidebar.selectbox("Seleccionar año", anios)
mesSelec = st.sidebar.selectbox("Seleccionar mes", mes_sorted)

# Grafica comparativa de mes por los dos años

del dfCafe[dfCafe.columns[0]]

dfFiltradoMesanio = dfCafe[(dfCafe["fechaEntrada"].dt.month_name() == mesSelec) & (dfCafe["fechaEntrada"].dt.year == anioSelec)]
dfMes = dfFiltradoMesanio.groupby(pd.Grouper(key="fechaEntrada",freq="1D")).count().reset_index()
dfMes["fechaStr"]= dfMes["fechaEntrada"].astype(str) + " - "
dfMes["Dia"] = dfMes["fechaEntrada"].dt.day_name() + " - " + dfMes["fechaStr"]

st.dataframe(dfFiltradoMesanio)

# Grafica por mes seleccionado

fig = px.bar(dfMes, x="Dia", y="horaEntrada", labels={"horaEntrada":"Numero de clientes"}, title="Numero de clientes por semana")
st.plotly_chart(fig, use_container_width=True)

# Grafica de los dos meses

dfmeses = dfCafe.groupby(pd.Grouper(key="fechaEntrada",freq="1M")).count().reset_index()
dfmeses['Año'] = dfmeses['fechaEntrada'].dt.year
dfmeses["Año"]= dfmeses["fechaEntrada"].dt.year.astype(str)
dfmeses["Mes"]= dfmeses["fechaEntrada"].dt.month_name().astype(str)

fig2 = px.bar(dfmeses, x="Mes", y="horaEntrada", barmode= "group", color='Año',height=400)
st.plotly_chart(fig2, use_container_width=True)

# Grafica de dias segun mes seleccionado

dfSemanas = dfFiltradoMesanio.groupby(pd.Grouper(key="fechaEntrada",freq="1W")).count().reset_index()

fig3 = px.bar(dfSemanas, x='fechaEntrada', y='horaEntrada', labels={'fechaEntrada': 'Mes', 'horaEntrada': 'Número de Clientes'}, title="Número de Clientes por Mes")
st.plotly_chart(fig3, use_container_width=True)
