import streamlit as st

st.set_page_config(page_title="StackOverflow Weekly Newsletter", page_icon=":computer:")

st.sidebar.title("Newsletter Options")
selected_date = st.sidebar.selectbox("Select Date", df['CREATION_DATE'].sort_values(ascending=False).unique())
search_term = st.sidebar.text_input("Search by keyword")

# Filter data based on user selection
filtered_df = df[df['CREATION_DATE'] == selected_date]
if search_term:
    filtered_df = filtered_df[filtered_df['NEWSLETTER_BODY'].str.contains(search_term, case=False)]

res_text = filtered_df.iloc[0]['NEWSLETTER_BODY'] if not filtered_df.empty else "No results found."

st.title("StackOverflow Weekly Programming Newsletter :computer:")
st.write(
    """This newsletter was generated based on StackOverflow questions and answers using an AI model."""
)

st.markdown(res_text)
