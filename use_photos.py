import streamlit as st
import pandas as pd
from doquery import do_query

def photos(engine, params):
    # Відображення списку фотографій
    sql_query = "select * from photos"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, 1:2]    # Обмежимо відображення рядком назви

    # Обмежимо ширину таблиці в px
    sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun", width=500)
    # sel = st.dataframe(df, selection_mode="single-row", on_select="rerun")
    sel_rows = sel["selection"]["rows"]

    col1, col2 = params
    # with col2:
    #     st.write(" ")

    # Фото відобразимо зліва
    with col2:
        if len(sel_rows) > 0:
            nrow = sel_rows[0]
            row = results[nrow]
            name = row[1]
            comment = row[3]
            photo = row[2]
            st.subheader(":blue[" + name + "]")
            width = st.slider("Ширина", 200, 1000, 400, 10)
            st.image("images/" + photo, width=width)
            # st.image("images/" + photo)
            if comment is not None:
                st.write(comment)
