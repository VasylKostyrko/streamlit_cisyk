import streamlit as st
from use_biography import biography
from use_albums import albums
from use_photos import photos
from use_videos import videos


def section(engine, sel_row, params):
    if sel_row == 0:
        st.subheader(":blue[Біографія]")
        # st.subheader("Біографія")
        biography(engine)
    elif sel_row == 1:
        st.subheader(":blue[Альбоми пісень]")
        ret = albums(engine, params)
    elif sel_row == 2:
        st.subheader(":blue[Фотоальбом]")
        photos(engine, params)
    elif sel_row == 3:
        st.subheader(":blue[Відео про Квітку Цісик]")
        videos(engine, params)
