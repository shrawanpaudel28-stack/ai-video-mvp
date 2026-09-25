import streamlit as st
import replicate

st.set_page_config(
    page_title="My AI Video Creator",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 My AI Video Creator")
st.write("Create a short AI-generated video from your idea.")

st.header("1. Write your video idea")

idea = st.text_area(
    "What should the video be about?",
    placeholder=(
        "Example: A small friendly robot stands in a colourful garden. "
        "A yellow butterfly lands on the robot's hand."
    ),
    height=140
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
        "Vertical 9:16 for YouTube Shorts or TikTok",
        "Wide 16:9 for YouTube",
        "Square 1:1 for Instagram"
    ]
)

st.warning(
    "This creates a real AI video and may use Replicate credits. "
    "For now, generate only one short test video."
)

if st.button("🎬 Generate my short video", type="primary"):

    if idea.strip() == "":
        st.warning("Please write a video idea first.")

    elif "REPLICATE_API_TOKEN" not in st.secrets:
        st.error(
            "Your Replicate token cannot be found. "
            "Go to Streamlit App Settings → Secrets and save it again."
        )

    else:
        prompt =
