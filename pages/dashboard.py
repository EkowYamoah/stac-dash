import numpy as np
import pandas as pd
import plotly.express as px

import streamlit as st
from datetime import datetime,date
st.set_page_config(page_title="Dashboard",layout="wide")

#Global Variables
today = datetime.now().strftime("%m-%d-%Y")
df = pd.read_csv("data.csv")


headerSection = st.container() 
mainSection = st.container()
leftNav = st.sidebar

##KPIs
totalEnrolledFarmers = df['Total_Farmers_Enrolled'].sum()

# Format totalEnrolledFarmers with commas for thousands
formatted_total = '{:,}'.format(totalEnrolledFarmers)

totalFarmerPopulation = 120000
totalEnrolledPercentage = round((totalEnrolledFarmers/totalFarmerPopulation)*100,2)
# print("Area = {:.2f}".format(area))

#RING KPIs 
try:
    if totalEnrolledFarmers > 0:
        AVC_0_0 = (df['Farmers_0_0_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_2_5 = (df['Farmers_2_5_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_5_0 = (df['Farmers_5_0_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_7_5 = (df['Farmers_7_5_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_10_0 = (df['Farmers_10_0_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_12_5 = (df['Farmers_12_5_AVC'].sum() / totalEnrolledFarmers) * 100
        AVC_15_0 = (df['Farmers_15_0_AVC'].sum() / totalEnrolledFarmers) * 100
except ZeroDivisionError:
    pass


    

with mainSection:
    # st.write(f"Date: {today}")

    
    left_col,right_col = st.columns(2)
    
    with left_col:
         # Get the current theme
        theme = st.session_state.theme if 'theme' in st.session_state else 'light'

        # Define custom CSS classes for light and dark themes
        light_theme_style = """
            <style>
                .custom-card {
                    background-color: #27005D;
                    color:white;
                    padding: 10px;
                    border-radius: 10px;
                }
            </style>
        """

        dark_theme_style = """
            <style>
                .custom-card {
                    background-color: #27005D;
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                }

                h4{
                color: white;
                }
            </style>
        """

        # Set the appropriate style based on the theme
        if theme == 'light':
            st.markdown(light_theme_style, unsafe_allow_html=True)
        else:
            st.markdown(dark_theme_style, unsafe_allow_html=True)

        # Content inside the card
        st.markdown(
            f"""
            <div class="custom-card">
                <h4 style="margin: 0;color: white; padding: 0;">TOTAL FARMERS ENROLLED</h4>
                <p style="margin: 0; padding: 0;">To date</p>
                <h2 style="margin: 0; color: white;padding: 0;">{formatted_total}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Create a DataFrame for the bar chart
        data = {
        'AVC Percentage': ['0%     AVC', '2.5%   AVC', '5.0%   AVC', '7.5%   AVC', '10.0%  AVC', '12.5%  AVC', '15.0%  AVC'],
        'Total AVC': [
            df['Farmers_0_0_AVC'].sum(),
            df['Farmers_2_5_AVC'].sum(),
            df['Farmers_5_0_AVC'].sum(),
            df['Farmers_7_5_AVC'].sum(),
            df['Farmers_10_0_AVC'].sum(),
            df['Farmers_12_5_AVC'].sum(),
            df['Farmers_15_0_AVC'].sum()
        ],
        'Color': ['#FF5733', '#FF9933', '#FFC300', '#33FF4B', '#33FFF1', '#336BFF', '#9133FF']
            }
    
        # Create a Plotly bar chart with color mapping
        fig = px.bar(
            data, x='AVC Percentage', y='Total AVC', color='Color',
            labels={'Total AVC': 'Total AVC'},
            color_discrete_map={'0%     AVC': '#FF5733', '2.5%   AVC': '#FF9933', '5.0%   AVC': '#FFC300',
                        '7.5%   AVC': '#33FF4B', '10.0%  AVC': '#33FFF1', '12.5%  AVC': '#336BFF', '15.0%  AVC': '#9133FF'}
                )

        # Customize chart appearance (e.g., labels, title)
        fig.update_layout(
            xaxis_title='AVC Percentage Category',
            yaxis_title='Total AVC',
            title='TOTAL AVC BREAKDOWN'
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig,use_container_width=False)



#RIGHT COLUMN

    with right_col:
       
       # Set the appropriate style based on the theme
        if theme == 'light':
            st.markdown(light_theme_style, unsafe_allow_html=True)
        else:
            st.markdown(dark_theme_style, unsafe_allow_html=True)

        # Content inside the first card (ENROLLED PERCENTAGE)
        st.markdown(
            f"""
            <div class="custom-card">
                <h4 style="margin: 0; color: white;padding: 0;">ENROLLED PERCENTAGE</h4>
                <p style="margin: 0; padding: 0;">Of Total Farmer Population</p>
                <h2 style="margin: 0; color: white;padding: 0;">{totalEnrolledPercentage}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Group and count the number of occurrences for each region
        column_sums = df['Region'].value_counts().reset_index()
        column_sums.columns = ['Region', 'Count']

                # Create a Plotly bar chart
        fig = px.bar(
            column_sums, x='Region', y='Count',
            color='Region',
            labels={'Count': 'Total Enrolment'},
        )

            # Customize chart appearance (e.g., labels, title)
        fig.update_layout(
            xaxis_title='Region',
            yaxis_title='Total Enrolment',
            title='TOTAL ENROLMENT BY REGIONAL BREAKDOWN'
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
        

        

      


st.markdown("---")




left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

st.table(df)
        
        







# PIE CHARTS

st.header("ENROLLED PERCENTAGE BY REGIONS")
fig = px.pie(df,values = "Total_Farmers_Enrolled", names="Region", hole = 0.5)
# fig.update_traces(text = filtered_df['Region'], textposition="outside"
st.plotly_chart(fig, use_container_width=False)









#     map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)
      
