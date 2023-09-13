import streamlit as st

st.set_page_config(
    page_title = "Multipage App",
)

st.title("Main Page")
st.sidebar.success("Select Page from above")

st.title('Counter Example')
increment = st.button('Increment')
count = 0
if increment:
    count += 1

st.write('count = ', count)