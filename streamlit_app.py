import streamlit as st
import snowflake.connector

# Write directly to the app
st.title("Stackoverflow Weekly Programming Newsletter :computer:")
st.write(
    """This newsletter was generated based on stackoverflow questions and answers using an AI model
    """
)

# Get the current credentials

conn = snowflake.connector.connect(
    user='fsoufary',
    password='$(echoLiiamra1)',
    account='lm93303.eu-central-1',
    warehouse='compute_wh',
    database='pfe2024',
    schema='stackoverflow'
)
cursor = conn.cursor()


# Execute the query and fetch the data into a Pandas DataFrame
query = "SELECT * FROM newsletters"
cursor.execute(query)
table_pandas_df = cursor.fetch_pandas_all()

res_text = table_pandas_df.loc[table_pandas_df['CREATION_DATE'].idxmax()]['NEWSLETTER_BODY']
st.markdown(res_text)



