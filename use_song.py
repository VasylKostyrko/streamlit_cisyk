import streamlit as st


def song(row,params):
    name = row[2]
    eng_name = row[3]
    duration = row[4]
    words = row[5]
    music = row[6]
    video = row[7]
    text = row[8]

    with st.container(border=True):
        col1, col2 = params
        with col1:
            st.divider()
            st.divider()
            st.divider()
            st.subheader("Пісня: :blue[" + name + "]")
            # st.subheader("Пісня: " + name)
            st.write("Назва в альбомі: " + eng_name)
            st.write("Тривалість: " + duration)
            st.write("Слова: " + words)
            st.write("Музика: " + music)
            st.video(video)

        with col2:
            st.divider()
            st.subheader(":blue[Слова пісні]")
            st.write(text, unsafe_allow_html=True)


def eng_song(row,params):
    name = row[2]
    eng_name = row[3]
    duration = row[4]
    video = row[5]
    comment = row[6]

    with st.container(border=True):
        col1, col2 = params
        with col1:
            st.divider()
            st.divider()
            st.divider()
            st.subheader("Пісня: :blue[" + eng_name + "]")
            st.write(name)
            st.write("Тривалість: " + duration)
            st.write(comment)
            st.video(video)

