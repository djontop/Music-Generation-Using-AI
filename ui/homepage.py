import streamlit as st
from streamlit_option_menu import option_menu

from ui import music_page, model_page, history_page, about_page


def homepage():
    with st.sidebar:
        st.title("Musc")
        st.caption("music from nowhere")
        st.divider()
        selected = option_menu(
            menu_title=None,
            options=["Melody", "Models"],
            icons=["music-note-beamed", "gear", "clock", "info-circle"]
        )
    if selected == "Melody":
        music_page.main()
    elif selected == "Models":
        model_page.model_page()
    elif selected == "History":
        history_page.history_page()
    elif selected == "About":
        about_page.about_page()
