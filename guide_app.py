import streamlit as st
import json
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import tempfile
# Optional: for generation if key is provided
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Page Config
st.set_page_config(page_title="Persona Cloning Tool", layout="wide")

# Session State Initialization
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "character_config" not in st.session_state:
    st.session_state.character_config = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for API Keys and Config
st.sidebar.title("Configuration")
openai_api_key = st.sidebar.text_input("OpenAI API Key (Optional)", type="password")

st.title("🤖 Persona Cloning & Interaction Tool")
st.markdown("""
This tool allows you to:
1. **Define** a character persona.
2. **Ingest** their past writings to learn their style ("Scan").
3. **Interact** with the cloned persona using RAG (Retrieval Augmented Generation).
""")

tabs = st.tabs(["1. Define Persona", "2. Ingest Data (Scan)", "3. Interact (Clone)", "4. Guide"])

# --- TAB 1: DEFINE PERSONA ---
with tabs[0]:
    st.header("Define Character Persona")

    # Load default if nothing loaded
    if st.session_state.character_config is None:
        try:
            with open("example.json", "r") as f:
                st.session_state.character_config = json.load(f)
        except:
            st.session_state.character_config = {}

    # Editor
    config_str = st.text_area("Character JSON Bible", value=json.dumps(st.session_state.character_config, indent=2), height=400)

    if st.button("Save Configuration"):
        try:
            st.session_state.character_config = json.loads(config_str)
            st.success("Configuration saved!")
        except json.JSONDecodeError:
            st.error("Invalid JSON format.")

# --- TAB 2: INGEST DATA ---
with tabs[1]:
    st.header("Ingest Data (Scan Style)")
    st.markdown("Upload text files containing the person's past messages, blogs, or posts.")

    uploaded_files = st.file_uploader("Upload Text Files", accept_multiple_files=True, type=['txt', 'md', 'json'])

    if st.button("Process & Index"):
        if not uploaded_files:
            st.warning("Please upload files first.")
        else:
            with st.spinner("Processing files and building vector index... (This may take a moment)"):
                documents = []
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

                for uploaded_file in uploaded_files:
                    # Read content
                    content = uploaded_file.read().decode("utf-8")
                    # Create document
                    doc = Document(page_content=content, metadata={"source": uploaded_file.name})
                    # Split
                    chunks = text_splitter.split_documents([doc])
                    documents.extend(chunks)

                if documents:
                    # Initialize Embeddings (Local)
                    # using a small model for speed in demo
                    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

                    # Create Qdrant Collection in memory
                    # For persistence, we would use path="local_qdrant"
                    st.session_state.vector_store = Qdrant.from_documents(
                        documents,
                        embeddings,
                        location=":memory:",  # In-memory for session duration
                        collection_name="persona_style"
                    )
                    st.success(f"Successfully indexed {len(documents)} chunks from {len(uploaded_files)} files.")
                else:
                    st.warning("No text content found.")

# --- TAB 3: INTERACT ---
with tabs[2]:
    st.header("Chat with Cloned Persona")

    if st.session_state.vector_store is None:
        st.warning("⚠ No data ingested yet. Please go to the 'Ingest Data' tab and upload content first.")

    # Chat Interface
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Say something..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Response
        with st.chat_message("assistant"):
            if st.session_state.vector_store:
                # 1. Retrieve Context
                docs = st.session_state.vector_store.similarity_search(prompt, k=3)
                context_text = "\n\n".join([d.page_content for d in docs])

                # 2. Construct System Prompt
                char_name = st.session_state.character_config.get("name", "AI")
                traits = ", ".join(st.session_state.character_config.get("core_traits", []))
                style = st.session_state.character_config.get("speech_style", {})

                system_prompt = f"""You are {char_name}.
Traits: {traits}
Speaking Style: {style}

Below are some examples of your past writing/speaking (Context):
---
{context_text}
---

Reply to the user's message in your style, using the context if relevant.
"""

                # 3. Call LLM if key exists, else Mock
                response_text = ""
                if openai_api_key:
                    try:
                        llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7)
                        msgs = [
                            SystemMessage(content=system_prompt),
                            HumanMessage(content=prompt)
                        ]
                        res = llm(msgs)
                        response_text = res.content
                    except Exception as e:
                        response_text = f"Error calling OpenAI: {e}"
                else:
                    response_text = "**(Simulation Mode - No API Key)**\n\n"
                    response_text += f"**System Prompt Constructed:**\n\n```\n{system_prompt}\n```\n\n"
                    response_text += "**What would happen:** The LLM would use the `Context` chunks above (which are retrieved from your uploaded files) to mimic the style and content of the persona."

                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

            else:
                st.error("Please ingest data first.")

# --- TAB 4: GUIDE ---
with tabs[3]:
    st.markdown("### Original Guide Content")
    st.markdown("Use this reference to understand the broader pipeline.")

    # (Original Guide Logic Preserved lightly)
    steps = {
        "1. Preparing Assets": "Define JSON and gather samples.",
        "2. Infrastructure": "Setup vector DBs and hosting.",
        "3. Chat Persona": "Prompt engineering and RAG.",
        "4. Visuals": "Stable Diffusion and LoRAs.",
        "5. Voice/Video": "ElevenLabs and SadTalker."
    }

    st.json(steps)
    st.info("The tabs above implement the 'Chat Persona' and 'Infrastructure' parts of this guide directly in your browser!")
