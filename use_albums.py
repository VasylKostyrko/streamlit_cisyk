import streamlit as st
import pandas as pd
from doquery import do_query
from use_album import album


def albums(engine,params):
    # Вибір альбому пісень
    sql_query = "select * from albums"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, 1:2]
    sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    # nal = st.dataframe(df, selection_mode="single-row", on_select="rerun")
    sel_rows = sel["selection"]["rows"]
    if len(sel_rows) > 0:
        nrow = sel_rows[0]
        row = results[nrow]
        ind = row[0]
        name = row[1]
        date = row[3]
        level = row[4]
        title = "Альбом пісень :blue[" + '"' + name + '"]'
        # cdate = "Альбом пісень " + name
        if date is not None:
            title = title + ' (' + str(date) + ')'
        st.subheader(title)
        album(engine, ind, params, level)
