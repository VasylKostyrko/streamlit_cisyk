import streamlit as st
import pandas as pd
from doquery import do_query


def videos(engine, params):
    # Відображення списку відео про Квітку Цісик
    sql_query = "select * from videos"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, 1:2]  # Обмежимо відображення рядком назви
    # sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    # sel = st.dataframe(df, selection_mode="single-row", on_select="rerun")

    extend = st.checkbox("Всі рядки")
    if extend:
        row_height = 35
        header_height = 35  # Приблизна висота заголовка
        total_height = (len(df) * row_height) + header_height
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun", height=total_height)
    else:
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")

    sel_rows = sel["selection"]["rows"]
    col1, col2 = params

    with col1:
        if len(sel_rows) > 0:
            nrow = sel_rows[0]
            row = results[nrow]
            name = row[1]
            duration = row[2]
            url= row[3]
            st.subheader(":blue[" + name + "]")
            st.write("Тривалість: ", duration)
            st.video(url)
