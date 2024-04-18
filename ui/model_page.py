import streamlit as st

from ui import utility

def model_page():
    with st.container():
        st.title("Models")
        st.caption(
            "Generate of finetune models with custom datasets and manage them.")
        st.divider()
    model_names = utility.get_model_names()
    if len(model_names) > 0:
        with st.container():
            st.subheader("Available Models")
            for model in model_names:
                col_1, col_2, col_3 = st.columns([2, 2, 1])
                with col_1.container():
                    st.write(f"**{model}**")
                with col_2.container():
                    st.write(model_names[model])
                with col_3.container():
                    delete = st.button('Delete', key=model)
                    if delete:
                        utility.delete_model(model)
                        st.experimental_rerun()
            st.divider()