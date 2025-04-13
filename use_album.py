import streamlit as st
import pandas as pd
from doquery import do_query
from use_song import song, eng_song


def album(engine, nrow, params, level):
    # Будує таблицю з піснями вибраного альбому
    if level == 2:
        # Дворівневий вибір україномовних пісень
        sql_query = "select * from songs where album_id = " + str(nrow)
    else:
        # Однорівневий вибір англомовних саундтреків
        sql_query = "select * from engvideos where album_id = " + str(nrow)
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, 2:3]    # Обмежимо відображення рядком назви

    extend = st.checkbox("Всі рядки")
    if extend:
        row_height = 35
        header_height = 35  # Приблизна висота заголовка
        total_height = (len(df) * row_height) + header_height
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun", height=total_height)
    else:
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")

    # sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    # sel = st.dataframe(df, selection_mode="single-row", on_select="rerun")
    sel_rows = sel["selection"]["rows"]
    if len(sel_rows) > 0:
        nrow = sel_rows[0]
        row = results[nrow]
        if level == 2:
            # Дворівневий вибір україномовних пісень
            song(row, params)
        else:
            # Однорівневий вибір англомовних саундтреків
            eng_song(row, params)
