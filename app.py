import streamlit as st

st.set_page_config(
    page_title="My AI Video Creator",
    page_icon="🎬"
)

st.title("🎬 My AI Video Creator")
st.write("Create a 10-second AI video prompt.")

st.header("1. Write your video idea")

idea = st.text_area(
    "What should the video be about?",
    placeholder="Example: A friendly robot visits the moon."
)

st.header("2. Choose a character")

character = st.selectbox(
    "Choose one character:",
    [
        "Friendly Robot",
        "Cartoon Boy",
        "Cartoon Girl",
        "Fox",
        "Bear"
    ]
)

st.header("3. Choose a style")

style = st.selectbox(
    "Choose a video style:",
    [
        "2D Cartoon",
        "3D Animation",
        "Storybook",
        "Educational"
    ]
)

st.header("4. Choose video shape")

video_shape = st.selectbox(
    "Where will you post the video?",
    [
        "Vertical for YouTube Shorts / TikTok (9:16)",
        "Wide for YouTube (16:9)",
        "Square for Instagram (1:1)"
    ]
)

if st.button("✨ Generate video prompt"):
    if idea.strip() == "":
        st.warning("Please write an idea first.")
    else:
        prompt = f"""
Create a high-quality 10-second {style} animated video.

Main character: {character}.

Story: {idea}

Video format: {video_shape}.
Use clear character actions, bright lighting, smooth animation,
a family-friendly tone, consistent character appearance, and no text on screen.
"""

        st.success("Your AI video prompt is ready!")

        st.subheader("Copy this prompt into a video AI")
        st.code(prompt, language="text")

        st.info(
            "The next step is to connect this app to a real video-generation AI. "
            "For now, you can copy the prompt and use it to test video tools."
        )
