import requests
import gradio as gr

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL_NAME = "phi3"
SYSTEM_PROMPT = "You are a helpful AI assistant."


def chat(message, history):
    """Send the current message and conversation history to local Ollama."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Support both newer Gradio message history and older tuple-based history.
    for item in history or []:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content")
            if role in ("user", "assistant") and isinstance(content, str):
                messages.append({"role": role, "content": content})
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            user_message, assistant_message = item[0], item[1]
            if isinstance(user_message, str) and user_message:
                messages.append({"role": "user", "content": user_message})
            if isinstance(assistant_message, str) and assistant_message:
                messages.append({"role": "assistant", "content": assistant_message})

    messages.append({"role": "user", "content": message})

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "messages": messages, "stream": False},
            timeout=180,
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]
    except requests.exceptions.ConnectionError:
        return (
            "I couldn't connect to Ollama. Make sure Ollama is installed and running, "
            "then run `ollama pull phi3` in your terminal."
        )
    except requests.exceptions.Timeout:
        return "The model took too long to respond. Please try again."
    except (requests.exceptions.RequestException, KeyError, ValueError) as exc:
        return f"Something went wrong while contacting Ollama: {exc}"


demo = gr.ChatInterface(
    fn=chat,
    title="Local AI Chatbot",
    description="Chat with Phi-3 running locally through Ollama.",
)

if __name__ == "__main__":
    demo.launch()
