import streamlit as st
import pandas as pd
from doquery import do_query
from use_section import section


def content(engine, params):
    # Перегляд таблиці змісту
    sql_query = "select * from content"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, 1:2]  # Обмежимо відображення рядком назви
    sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    # sel = st.dataframe(df, selection_mode="single-row", on_select="rerun")
    sel_rows = sel["selection"]["rows"]
    if len(sel_rows) > 0:
        sel_row = sel_rows[0]
        section(engine, sel_row, params)

