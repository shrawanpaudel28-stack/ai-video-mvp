import streamlit as st

st.set_page_config(
    page_title="My AI Video Creator",
    page_icon="🎬"
)

st.title("🎬 My AI Video Creator")
st.write("Welcome! We are building a 10-second AI video creator.")

st.header("1. Write your idea")

idea = st.text_area(
    "What should the video be about?",
    placeholder="Example: A friendly robot visits the moon."
)

st.header("2. Choose a character")

character = st.selectbox(
    "Choose one character:",
    ["Friendly Robot", "Cartoon Boy", "Cartoon Girl", "Fox", "Bear"]
)

st.header("3. Choose a style")

style = st.selectbox(
    "Choose a video style:",
    ["2D Cartoon", "3D Animation", "Storybook", "Educational"]
)

if st.button("Create my video idea"):
    if idea.strip() == "":
        st.warning("Please write an idea first.")
    else:
        st.success("Your video request is ready!")
        st.write("**Your idea:**", idea)
        st.write("**Character:**", character)
        st.write("**Style:**", style)
        st.info("Actual video generation will be added in the next step.")
