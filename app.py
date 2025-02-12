import pandas as pd
import numpy as np
import streamlit as stl
import wrangle as wr
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_card import card

# reading data
# df = pd.read_excel("VIBE.xlsx", sheet_name=None)
# data = df.get('Summary YiW Dec2024 Primary')
# df = wr.wrangle(data)

# page configurating
stl.set_page_config(page_title="Tool",
                    page_icon=":bar_chart:", layout="wide")
stl.write('<br>')

stl.markdown(
    '<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
# File uploader
fl = stl.file_uploader(":file_folder: Upload file", type=["xlsx", "xls"])

if fl is not None:
    # Read the uploaded file
    df = pd.read_excel(fl,sheet_name=None)
    data = df.get('Summary YiW Dec2024 Primary')
    df = wr.wrangle(data)
    # stl.write(df.columns)

    # sidebar
    stl.header("Summary YiW progress of December 2024-Primary YIW")
    stl.sidebar.header("Select Your Filter")
    project = stl.sidebar.selectbox(


        "Select Project", df["Projects"].unique(), index=None)

    # deviding page into two columns
    kpi1, kpi2, kpi3, kpi4, kpi5 = stl.columns(5)

    outreach_col, supported_col = stl.columns(2)
    if project != None:
        filtered_df = df.loc[df['Projects'] == project]
        cumulative = wr.cumulative(filtered_df)
        normal = wr.normal(filtered_df)
        refuge = wr.refuge(filtered_df)
        community = wr.community(filtered_df)
        pwd = wr.pwd(filtered_df)

        col_1, col_2 = stl.columns(2)
        with col_1:
            # ============================================ cumulative ==============================
            # Extract columns and values
            categories = cumulative.columns
            values = cumulative.iloc[0]  # Selecting the first (only) row

            # Create a bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                text=values,  # Adding text labels
                textposition="auto",
                marker_color=["blue", "pink", "lightblue"]  # Custom colors
            ))

            # Customize Layout
            fig.update_layout(
                title={
                    "text": f"{project} Cumulative",
                    "x": 0.5,  # Center the title horizontally
                    "y": 0.95,  # Adjust the vertical position (closer to the top)
                    "xanchor": "center",
                    "yanchor": "top"
                },
                # xaxis_title="Category",
                yaxis_title="Count",
                height=500,  # Adjust figure size
                width=400
            )
            stl.plotly_chart(fig)

            stl.write()
    # ====================================== Refuges =====================================================
            categories = refuge.columns
            values = refuge.iloc[0]  # Selecting the first (only) row

            # Create a bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                text=values,  # Adding text labels
                textposition="auto",
                marker_color=["blue", "pink", "lightblue"]  # Custom colors
            ))

            # Customize Layout
            fig.update_layout(
                title={
                    "text": f"{project} Reguges",
                    "x": 0.5,  # Center the title horizontally
                    "y": 0.95,  # Adjust the vertical position (closer to the top)
                    "xanchor": "center",
                    "yanchor": "top"
                },
                # xaxis_title="Category",
                yaxis_title="Count",
                height=500,  # Adjust figure size
                width=400
            )
            stl.plotly_chart(fig)

            stl.write()
    # ====================================== pwd ===================================================
            categories = pwd.columns
            values = pwd.iloc[0]  # Selecting the first (only) row

            # Create a bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                text=values,  # Adding text labels
                textposition="auto",
                marker_color=["blue", "pink", "lightblue"]  # Custom colors
            ))

            # Customize Layout
            fig.update_layout(
                title={
                    "text": f"{project} PWD",
                    "x": 0.5,  # Center the title horizontally
                    "y": 0.95,  # Adjust the vertical position (closer to the top)
                    "xanchor": "center",
                    "yanchor": "top"
                },
                # xaxis_title="Category",
                yaxis_title="Count",
                height=500,  # Adjust figure size
                width=400
            )
            stl.plotly_chart(fig)
        with col_2:
            # ============================================= Normal ================================
            # Extract columns and values
            categories = normal.columns
            values = normal.iloc[0]  # Selecting the first (only) row

            # Create a bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                text=values,  # Adding text labels
                textposition="auto",
                marker_color=["blue", "pink", "lightblue"]  # Custom colors
            ))

            # Customize Layout
            fig.update_layout(
                title={
                    "text": f"{project} Normal",
                    "x": 0.5,  # Center the title horizontally
                    "y": 0.95,  # Adjust the vertical position (closer to the top)
                    "xanchor": "center",
                    "yanchor": "top"
                },
                # xaxis_title="Category",
                yaxis_title="Count",
                height=500,  # Adjust figure size
                width=400
            )
            stl.plotly_chart(fig)

            stl.write()
            # ========================================= comminity ===============================
            categories = community.columns
            values = community.iloc[0]  # Selecting the first (only) row

            # Create a bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                text=values,  # Adding text labels
                textposition="auto",
                marker_color=["blue", "pink", "lightblue"]  # Custom colors
            ))

            # Customize Layout
            fig.update_layout(
                title={
                    "text": f"{project} Host Community",
                    "x": 0.5,  # Center the title horizontally
                    "y": 0.95,  # Adjust the vertical position (closer to the top)
                    "xanchor": "center",
                    "yanchor": "top"
                },
                # xaxis_title="Category",
                yaxis_title="Count",
                height=500,  # Adjust figure size
                width=400
            )
            stl.plotly_chart(fig)

    else:
        with stl.container():
            with kpi1:

                card1 = card(
                    title=f"{df['Total YIW'].sum()}",
                    text="Total YIW",
                    styles={
                        "card": {
                            "width": "120%",
                            "height": "100px",
                            "background-color": "#f0f8ff",  # Add your desired background color
                            "border-radius": "5px",

                        }
                    }
                )
            with kpi2:

                card2 = card(
                    title=f"{df['Total youth in Work'].sum()}",
                    text="Total youth in Work",
                    styles={
                        "card": {
                            "width": "120%",
                            "height": "100px",
                            "background-color": "#f0f8ff",  # Add your desired background color
                            "border-radius": "5px",

                        }
                    }
                )
            with kpi3:

                card3 = card(
                    title=f"{df['Total Youth refugees in Work'].sum()}",
                    text="Total Youth refugees in Work",
                    styles={
                        "card": {
                            "width": "120%",
                            "height": "100px",
                            "background-color": "#f0f8ff",  # Add your desired background color
                            "border-radius": "5px",

                        }
                    }
                )
            with kpi4:

                card4 = card(
                    title=f"{df['Total Youth Host community in Work'].sum()}",
                    text="Total Youth Host community in Work",
                    styles={
                        "card": {
                            "width": "120%",
                            "height": "100px",
                            "background-color": "#f0f8ff",  # Add your desired background color
                            "border-radius": "5px",

                        }
                    }
                )
            with kpi5:

                card4 = card(
                    title=f"{df['Total Youth PWD in work'].sum()}",
                    text="Total Youth PWD in work",
                    styles={
                        "card": {
                            "width": "120%",
                            "height": "100px",
                            "background-color": "#f0f8ff",  # Add your desired background color
                            "border-radius": "5px",

                        }
                    }
                )
        with stl.container():
            with outreach_col:
                
                fig = px.bar(df[['Projects', 'Outreach']].sort_values(
                    by='Outreach'), x='Projects', y='Outreach', text='Outreach', title='Outreach per Project')

                # Customize layout
                fig.update_traces(textposition='outside', marker_color='royalblue')
                fig.update_layout(
                    xaxis_tickangle=-45,
                    width=400,
                    height=540
                )
                stl.plotly_chart(fig)

            with supported_col:
                fig = px.bar(df[['Projects', 'Supported(MSMEs)']].sort_values(
                    by='Supported(MSMEs)'), x='Projects', y='Supported(MSMEs)', text='Supported(MSMEs)', title='Supported(MSMEs) per Project')

                # Customize layout
                fig.update_traces(textposition='outside', marker_color='royalblue')
                fig.update_layout(
                    xaxis_tickangle=-45,
                    width=400,
                    height=540
                )
                stl.plotly_chart(fig)
else:
    stl.write(":warning: Please upload an Excel file to proceed.")