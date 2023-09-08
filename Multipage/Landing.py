import streamlit as st

st.set_page_config(
    page_title = "Multipage App",
)

st.title("Main Page")
st.sidebar.success("Select Page from above")

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('count = ', st.session_state.count)