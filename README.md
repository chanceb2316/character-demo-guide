# Character-Persistent AI Demo Guide

This Streamlit app helps you build and showcase a consistent AI character across chat, voice, and video using lightweight, mostly free services.

## 🚀 Features
- Step-by-step guide with dropdown navigation
- Hyperlinks to free-tier tools and services
- Visual placeholders and prompt templates
- Deep dive buttons for each step
- PDF and Markdown export options
- QR code generator for mobile sharing
- Progress tracker and character config loader

## 🧪 How to Run Locally

```bash  
pip install -r requirements.txt
streamlit run guide_app.py
```

## 🌐 How to Deploy Online

### Option 1: Streamlit Cloud
- Go to Streamlit Cloud
- Connect your GitHub repo
- Select guide_app.py as the app entry point
- Add any secrets (like API keys) via the web UI

### Option 2: Hugging Face Spaces
- Create a new Space using the Streamlit SDK
- Upload your files and assets
- Hugging Face will auto-deploy your app
- Share the Space URL with investors or generate a QR code

### Option 3: Render or Railway
- Create a new web service
- Use this start command:
  `bash
  streamlit run guide_app.py --server.port $PORT --server.address 0.0.0.0
  `
- Set environment variables for secrets
- Choose a free tier for lightweight hosting

---

## 📱 Android Access

- Open your deployed URL in Chrome
- Tap the menu → “Add to Home screen” for app-like experience
- Or wrap the URL in a WebView for a native Android app
- For QR sharing, use the built-in QR generator in the app

---

## 📁 Folder Structure

#### character-demo-guide  
├── guide_app.py  
├── requirements.txt  
├── README.md  
├── elara_v1.json  
├── assets/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── placeholder1.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── placeholder2.png


## 🧠 Character Config

Use elara_v1.json as your sample character bible. You can load it into the app to personalize the guide and test your character pipeline.

This JSON defines:
- Core traits and philosophy
- Speech style and quirks
- Visual appearance and props
- Voice characteristics
- Boundaries and catchlines

You can swap in your own character by editing or uploading a new JSON file inside the app.
