import streamlit as st
import replicate

st.set_page_config(
    page_title="My AI Video Creator",
    page_icon="🎬"
)

st.title("🎬 My AI Video Creator")
st.write("Create a short AI-generated video from your idea.")

st.header("1. Write your video idea")

idea = st.text_area(
    "What should the video be about?",
    placeholder="Example: A friendly robot waves to a butterfly in a colourful garden."
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
    "Generating a video can use Replicate credits. "
    "Create only one short test video first."
)

if st.button("🎬 Generate my short video"):
    if idea.strip() == "":
        st.warning("Please write an idea first.")
    elif "REPLICATE_API_TOKEN" not in st.secrets:
        st.error("Your Replicate token is missing. Add it in Streamlit Secrets.")
    else:
        prompt = f"""
A high-quality 5-second {style} animated video.

Main character: {character}.

Story: {idea}

Format: {video_shape}.
Bright lighting, clear action, family-friendly, smooth motion,
consistent character appearance, no subtitles, no text on screen.
"""

        st.subheader("Your video instruction")
        st.code(prompt, language="text")

        try:
            with st.spinner("Creating your video. This can take a few minutes..."):
                client = replicate.Client(
                    api_token=st.secrets["REPLICATE_API_TOKEN"]
                )

                output = client.run(
                    "thudm/cogvideox-t2v",
                    input={
                        "prompt": prompt
                    }
                )

            st.success("Your video is ready!")

            if isinstance(output, list):
                video_url = output[0]
            else:
                video_url = output

            st.video(video_url)
            st.markdown(f"[Download your video]({video_url})")

        except Exception as error:
            st.error("The video could not be generated.")
            st.exception(error)
