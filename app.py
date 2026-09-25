import streamlit as st
import replicate

st.set_page_config(
    page_title="My AI Video Creator",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 My AI Video Creator")
st.write("Create a short AI-generated video from your idea.")

idea = st.text_area(
    "What should the video be about?",
    placeholder="Example: A friendly robot sees a butterfly in a colourful garden.",
    height=140
)

character = st.selectbox(
    "Choose a character:",
    ["Friendly Robot", "Cartoon Boy", "Cartoon Girl", "Fox", "Bear"]
)

style = st.selectbox(
    "Choose a video style:",
    ["2D Cartoon", "3D Animation", "Storybook", "Educational"]
)

video_shape = st.selectbox(
    "Where will you post the video?",
    [
        "Vertical 9:16 for YouTube Shorts or TikTok",
        "Wide 16:9 for YouTube",
        "Square 1:1 for Instagram"
    ]
)

st.warning("Generating a real AI video may use Replicate credits. Generate only one test video.")

if st.button("🎬 Generate my short video", type="primary"):

    if idea.strip() == "":
        st.warning("Please write a video idea first.")

    elif "REPLICATE_API_TOKEN" not in st.secrets:
        st.error("Replicate token is missing. Check Streamlit App Settings and Secrets.")

    else:
        prompt = (
            "Create a high-quality 5-second " + style + " animated video. "
            "Main character: " + character + ". "
            "Story: " + idea + " "
            "Video format: " + video_shape + ". "
            "Use bright lighting, clear action, smooth motion, a family-friendly tone, "
            "consistent character appearance, no subtitles, and no text on screen."
        )

        st.subheader("Video instruction sent to AI")
        st.code(prompt, language="text")

        try:
            with st.spinner("Creating your video. This can take a few minutes..."):

                client = replicate.Client(
                    api_token=st.secrets["REPLICATE_API_TOKEN"]
                )

                output = client.run(
                    "wavespeedai/wan-2.1-t2v-480p",
                    input={"prompt": prompt}
                )

            if isinstance(output, list):
                video_url = str(output[0])
            else:
                video_url = str(output)

            st.success("✅ Your AI video is ready!")
            st.video(video_url)
            st.link_button("Download your video", video_url)

        except Exception as error:
            st.error("The video could not be generated.")
            st.exception(error)

st.divider()
st.caption("Version 1: Text-to-video test.")
