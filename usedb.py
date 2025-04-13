import streamlit as st
from sqlalchemy import create_engine


def use_db():
    dbname = st.secrets["connection"]["url"]
    engine = create_engine(dbname)
    return engine
