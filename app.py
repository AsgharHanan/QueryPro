from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Query Pro", page_icon=":speech_ballon:")

st.title("Query Pro")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")

    st.text_input("Host", value="localhost")
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", type="password", value="admin")
    st.text_input("Database", value="Chinook")

    st.button("Connect")