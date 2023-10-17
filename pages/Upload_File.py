import pandas as pd
import streamlit as st
from datetime import datetime,date

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as part of the filename
filename1 = f'fileUpload-{current_datetime.strftime("%Y-%m-%d-%H-%M-%S")}.csv'


# Function to append the DataFrame to a CSV file

def append_csv(df, file_name):
    try:
        # Load the existing template CSV
        template = pd.read_csv(file_name)

        # Concatenate the existing data with the new data
        concatenated_df = pd.concat([template, df], ignore_index=True)

        # Save the concatenated DataFrame back to the template file
        concatenated_df.to_csv(file_name, index=False)
        # st.success("Data appended to the file successfully.")
       
    except Exception as e:
        st.error(f"Error appending data to CSV file: {e}")




# Function to save the DataFrame as a CSV file
def save_csv(df, file_name):
    # filename1 = 'fileUpload-'+ datetime.now().strftime("%Y-%m-%d")+'.csv'

    try:
        # Load the template CSV to check headers
        template = pd.read_csv('data.csv')

        # Get the headers from the template and df
        headers_template = set(template.columns)
        headers_df = set(df.columns)

        # Check if the headers in template match the headers in df
        if headers_template != headers_df:
            missing_columns = headers_template.difference(headers_df)
            st.warning("The headers in the uploaded file are missing the following expected columns:")
            for column in missing_columns:
                st.write(column)
        else:
            
            append_csv(df, file_name)
            st.success("File uploaded successfully.")
            df.to_csv(file_name1, index=False)
               # Reset the app to the homepage after a brief delay (2 seconds)
            st.experimental_rerun()

    except Exception as e:
        st.error(f"Error uploading CSV file: {e}")
        

# Function to save the DataFrame as a CSV file
def save_uploaded(df, file_name):
    # filename1 = 'fileUpload-'+ datetime.now().strftime("%Y-%m-%d")+'.csv'

    try:
        # Load the template CSV to check headers
        template = pd.read_csv('data.csv')

        # Get the headers from the template and df
        headers_template = set(template.columns)
        headers_df = set(df.columns)

        # Check if the headers in template match the headers in df
        if headers_template != headers_df:
            missing_columns = headers_template.difference(headers_df)
            st.warning("The headers in the uploaded file are missing the following expected columns:")
            for column in missing_columns:
                st.write(column)
        else:
            
            append_csv(df, file_name)
            st.success("File saved successfully.")
            df.to_csv(file_name, index=False)
               # Reset the app to the homepage after a brief delay (2 seconds)
            st.experimental_rerun()

    except Exception as e:
        st.error(f"Error uploading CSV file: {e}")



        
# Streamlit app layout
st.title("File Upload")

uploaded_file = st.file_uploader("Upload a file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Get the filename
    file_name = uploaded_file.name

    # Extract the file extension (in lowercase)
    file_extension = file_name.split('.')[-1].lower()

    if file_extension in ['csv', 'xlsx']:
        try:
            # Read the file into a DataFrame
            if file_extension == 'csv':
                df = pd.read_csv(uploaded_file)
            elif file_extension == 'xlsx':
                df = pd.read_excel(uploaded_file, engine='openpyxl')

            # Display the DataFrame as a table
            st.table(df.head(4))

            # Button to save the DataFrame as a CSV file
            if st.button("Upload file"):
               
                save_csv(df, "data.csv")
                save_uploaded(df, filename1)
                
        except Exception as e:
            st.error(f"Error reading {file_extension.upper()} file: {e}")
    else:
        st.warning("Unsupported file format. Please upload a CSV or XLSX file.")
        
        

