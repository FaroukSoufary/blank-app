import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="StackOverflow Weekly Newsletter", page_icon=":computer:")

# Title and description
st.title("StackOverflow Weekly Programming Newsletter :computer:")
st.write(
    """This newsletter was generated based on StackOverflow questions and answers using an AI model."""
)

# Connect to Snowflake and fetch the newsletters data
conn = st.connection("snowflake")  # Assuming you have a connection set up in Streamlit's experimental connection manager
df = conn.query("SELECT * FROM newsletters")  # Fetch the newsletters table
df['CREATION_DATE'] = pd.to_datetime(df['CREATION_DATE'])  # Ensure dates are in datetime format

# Sidebar for filtering options
st.sidebar.title("Newsletter Options")
search_term = st.sidebar.text_input("Search by keyword", "")
selected_date = st.sidebar.date_input("Select Date", df['CREATION_DATE'].max())

# Filter logic
if search_term:
    filtered_df = df[df['NEWSLETTER_BODY'].str.contains(search_term, case=False)]
elif selected_date:
    # Find the newsletter with the closest date to the selected date
    filtered_df = df.iloc[(df['CREATION_DATE'].date() - selected_date.date()).abs().argsort()[:1]]
else:
    # Default behavior: show the latest newsletter
    filtered_df = df[df['CREATION_DATE'] == df['CREATION_DATE'].max()]

# Extract the newsletter content
if not filtered_df.empty:
    res_text = filtered_df.iloc[0]['NEWSLETTER_BODY']
else:
    res_text = "No results found for the selected criteria."

# Display the newsletter content
st.markdown(f"<div class='newsletter-body'>{res_text}</div>", unsafe_allow_html=True)


# Comments section
st.text_area("Leave a comment", placeholder="Share your thoughts about this newsletter...")
st.button("Submit Comment")
