# import px as px
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout='wide')


df = pd.read_csv('India.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0 , 'Overall Bharat')

st.sidebar.title('Bharat Data Viz')

selected_State = st.sidebar.selectbox('Select a state' , list_of_states)
primary = st.sidebar.selectbox('Select primary parameter' , sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select secondary parameter' , sorted(df.columns[5:]))



plot = st.sidebar.button('Plot Graph')

if plot:
    st.text(' -> size represent Primary parameter')
    st.text(' -> Color represent secondary parameter')
    if selected_State == 'Overall Bharat':
        fig = px.scatter_mapbox(df , lat = 'Latitude' , lon="Longitude" , size = primary , color=secondary ,zoom = 3, size_max=35,
                          mapbox_style="carto-positron" , width= 1200 , height=700 , hover_name='District' , color_continuous_scale= px.colors.sequential.Viridis)

        st.plotly_chart(fig , use_container_width=True)
    else:
        state_df = df[df['State'] == selected_State]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon="Longitude", size=primary, color=secondary, zoom=3, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700 , hover_name='District' , color_continuous_scale= px.colors.sequential.Viridis)

        st.plotly_chart(fig, use_container_width=True)