import streamlit as st
import pandas as pd
from doquery import do_query


def biography(engine):
    # Перегляд рядків біографії співачки
    sql_query = "select * from biography"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    # sel = st.dataframe(df, selection_mode="single-row", on_select="rerun")
    df_lim = df.iloc[:, 1:3]

    extend = st.checkbox("Всі рядки")
    if extend:
        row_height = 35
        header_height = 35  # Приблизна висота заголовка
        total_height = (len(df) * row_height) + header_height
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun", height=total_height)
    else:
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    sel_rows = sel["selection"]["rows"]
    if len(sel_rows) > 0:
        nrow = sel_rows[0]
        row = results[nrow]
        st.header(":blue[Подія]")
        event = row[2]
        # st.write(":blue[" + event +"]")
        st.write(event)
        date = row[1]
        place = row[3]
        st.write(date, ", " + place)
        comment = row[4]
        print(comment)
        if comment is not None:
            st.write(comment)
