!pip install gradio requests -q

import gradio as gr
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-4o-mini"

def summarize(text, api_key):
    # --- Validation ---
    if not api_key or not api_key.strip():
        return "⚠️ Error: Please enter your API key."
    if not text or len(text.strip()) < 20:
        return "⚠️ Error: Text is too short. Please provide at least 20 characters."

    # --- Build the request ---
    headers = {
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a concise summarizer."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"},
        ],
        "temperature": 0.3,
    }

    # --- POST request ---
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.HTTPError as e:
        return f"❌ HTTP Error: {e}\n{response.text}"
    except Exception as e:
        return f"❌ Error: {e}"


# --- Gradio UI ---
with gr.Blocks(title="AI Summarizer") as demo:
    gr.Markdown("## 📝 AI Text Summarizer\nEnter your text and API key, then click **Summarize**.")

    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text to summarize",
                placeholder="Paste a paragraph, article, or notes here...",
                lines=8,
            )
        with gr.Column(scale=1):
            api_key_input = gr.Textbox(
                label="API Key",
                placeholder="sk-or-...",
                type="password",
            )
            summarize_btn = gr.Button("Summarize", variant="primary")

    output = gr.Textbox(label="Summary", lines=8, interactive=False)

    summarize_btn.click(
        fn=summarize,
        inputs=[text_input, api_key_input],
        outputs=output,
    )

demo.launch(share=True)
