import streamlit as st

st.set_page_config(page_title="Character-Persistent AI Demo Guide", layout="wide")

steps = {
    "1. Preparing Character Assets": [
        "Character JSON",
        "Few-shot Samples",
        "Reference Images/Videos"
    ],
    "2. Setting Up Free-Tier Infrastructure": [
        "GitHub & Asset Hosting",
        "Vector Memory (Qdrant)",
        "Middleware (Vercel)"
    ],
    "3. Implementing Chat Persona": [
        "System Prompt",
        "Memory Integration",
        "Consistency Checker"
    ],
    "4. Visual Consistency with Image Conditioning": [
        "Stable Diffusion",
        "Prompt Templates"
    ],
    "5. Avatar Video Generation": [
        "LivePortrait/SadTalker",
        "Colab Setup"
    ],
    "6. Assembling the Investor Demo": [
        "Web Demo",
        "Narrative Flow"
    ]
}

selected_main = st.sidebar.selectbox("Select Step", list(steps.keys()))
selected_sub = st.sidebar.selectbox("Select Sub-Step", steps[selected_main])

st.title("🚀 Character-Persistent AI Demo Guide")
st.markdown("This interactive guide walks you through building a consistent AI character across chat and video using lightweight, mostly free tools.")

def link(text, url):
    st.markdown(f"[{text}]({url})")

def show_visual(caption):
    st.image(f"https://via.placeholder.com/600x300.png?text={caption.replace(' ', '+')}", caption=caption)

def breakdown_button(step_name):
    if st.button(f"🔎 Break down '{step_name}' in depth"):
        st.markdown(f"### Detailed Breakdown: {step_name}")
        st.info(f"Here you could expand with code snippets, diagrams, or deeper explanations for **{step_name}**.")

st.header(f"{selected_main} → {selected_sub}")

if selected_main == "1. Preparing Character Assets":
    if selected_sub == "Character JSON":
        st.markdown("Define your character's identity in a structured JSON format.")
        link("JSON Schema", "https://json-schema.org")
        show_visual("Character JSON Structure")
        breakdown_button("Character JSON")

    elif selected_sub == "Few-shot Samples":
        st.markdown("Create dialogue and monologue samples to anchor your character's tone.")
        show_visual("Few-shot Sample Examples")
        breakdown_button("Few-shot Samples")

    elif selected_sub == "Reference Images/Videos":
        st.markdown("Collect consistent portraits and short clips for visual conditioning.")
        link("Instant-ID on Hugging Face", "https://huggingface.co/spaces/InstantX/InstantID")
        show_visual("Reference Image Example")
        breakdown_button("Reference Images/Videos")

elif selected_main == "2. Setting Up Free-Tier Infrastructure":
    if selected_sub == "GitHub & Asset Hosting":
        st.markdown("Use GitHub to store your assets and host static files.")
        link("GitHub", "https://github.com")
        link("GitHub Pages", "https://pages.github.com")
        show_visual("GitHub Repo Structure")
        breakdown_button("GitHub & Asset Hosting")

    elif selected_sub == "Vector Memory (Qdrant)":
        st.markdown("Use Qdrant Cloud to store and retrieve character memory snippets.")
        link("Qdrant Cloud", "https://qdrant.tech")
        show_visual("Qdrant Dashboard")
        breakdown_button("Vector Memory (Qdrant)")

    elif selected_sub == "Middleware (Vercel)":
        st.markdown("Use Vercel Functions to route prompts and inject character context.")
        link("Vercel", "https://vercel.com")
        show_visual("Vercel Function Flow")
        breakdown_button("Middleware (Vercel)")

elif selected_main == "3. Implementing Chat Persona":
    if selected_sub == "System Prompt":
        st.markdown("Craft a hidden system prompt that enforces character traits and boundaries.")
        show_visual("System Prompt Template")
        breakdown_button("System Prompt")

    elif selected_sub == "Memory Integration":
        st.markdown("Fetch top memory snippets from vector DB and inject into prompt.")
        show_visual("Memory Injection Flow")
        breakdown_button("Memory Integration")

    elif selected_sub == "Consistency Checker":
        st.markdown("Run a second LLM pass to score and regenerate off-character replies.")
        show_visual("Consistency Check Logic")
        breakdown_button("Consistency Checker")

elif selected_main == "4. Visual Consistency with Image Conditioning":
    if selected_sub == "Stable Diffusion":
        st.markdown("Use Instant-ID or IP-Adapter to condition image generation on reference photos.")
        link("IP-Adapter on Hugging Face", "https://huggingface.co/spaces/h94/IP-Adapter")
        show_visual("Stable Diffusion Conditioning")
        breakdown_button("Stable Diffusion")

    elif selected_sub == "Prompt Templates":
        st.markdown("Use structured prompts to guide consistent visual generation.")
        show_visual("Image Prompt Template")
        breakdown_button("Prompt Templates")

elif selected_main == "5. Avatar Video Generation":
    if selected_sub == "LivePortrait/SadTalker":
        st.markdown("Use free Colab notebooks to generate talking-head videos from portraits and audio.")
        link("LivePortrait GitHub", "https://github.com/KwaiVGI/LivePortrait")
        link("SadTalker GitHub", "https://github.com/OpenTalker/SadTalker")
        show_visual("Avatar Video Output")
        breakdown_button("LivePortrait/SadTalker")

    elif selected_sub == "Colab Setup":
        st.markdown("Run video generation notebooks on free Colab GPU instances.")
        link("Google Colab", "https://colab.research.google.com")
        show_visual("Colab Notebook Example")
        breakdown_button("Colab Setup")

elif selected_main == "6. Assembling the Investor Demo":
    if selected_sub == "Web Demo":
        st.markdown("Build a simple web interface to showcase chat and video outputs.")
        show_visual("Web Demo UI")
        breakdown_button("Web Demo")

    elif selected_sub == "Narrative Flow":
        st.markdown("Design a short story arc that highlights your character's consistency.")
        show_visual("Narrative Flow Diagram")
        breakdown_button("Narrative Flow")
