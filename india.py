import streamlit as st
import pandas as pd
import plotly.express as px

# Set your Mapbox access token
px.set_mapbox_access_token("your_mapbox_access_token_here")
st.set_page_config(layout="wide", page_title='India Data Visualization')
# Load data
df = pd.read_csv('India.csv')

# Prepare state list
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

# Sidebar inputs
st.sidebar.title('India Data Visualization')
selected_state = st.sidebar.selectbox('Select State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))
plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size Represents Primary Parameter')
    st.text('Color Represents Secondary Parameter')

    if selected_state == 'Overall India':
        # Plot for India
        fig = px.scatter_mapbox(
            df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
            zoom=5, mapbox_style="carto-positron", width=1200, height=700,
            hover_name="District"
        )
    else:
        # Plot for selected state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(
            state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
            zoom=6, mapbox_style="carto-positron", width=1200, height=700,
            hover_name="District"
        )

    st.plotly_chart(fig, use_container_width=True)
