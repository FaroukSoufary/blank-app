import streamlit as st
import pandas as pd

# Write directly to the app
st.title("StackOverflow Weekly Programming Newsletter :computer:")
st.write(
    """This newsletter was generated based on StackOverflow questions and answers using an AI model."""
)

# Connect to Snowflake and fetch the newsletters data
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM newsletters")  # Fetch the newsletters table
df['CREATION_DATE'] = pd.to_datetime(df['CREATION_DATE'])  # Ensure dates are in datetime format

# Sidebar for filtering options
search_term = st.text_input("Search by keyword", "")

# Filter logic
if search_term:
    filtered_df = df[df['NEWSLETTER_BODY'].str.contains(search_term, case=False)]
    if filtered_df.empty:
        st.write("No newsletters matched your search. Displaying the latest newsletter instead.")
        filtered_df = df[df['CREATION_DATE'] == df['CREATION_DATE'].max()]
else:
    # Default behavior: show the latest newsletter
    filtered_df = df[df['CREATION_DATE'] == df['CREATION_DATE'].max()]

# Extract the newsletter content
res_text = filtered_df.iloc[0]['NEWSLETTER_BODY']

# Display the newsletter content
st.markdown(res_text)
