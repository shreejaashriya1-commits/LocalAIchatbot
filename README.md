# Local AI Chatbot using Phi-3 and Ollama

A simple chatbot built with Python and Gradio. It sends prompts and conversation history to the Phi-3 language model running locally through Ollama.

## Technologies

- **Phi-3** — language model that generates responses
- **Ollama** — runs the model locally
- **Python** — chatbot backend
- **Requests** — sends HTTP requests to Ollama
- **Gradio** — provides the chat interface

## Requirements

- Python 3.10 or newer recommended
- Ollama installed on the computer running the application
- The Phi-3 model downloaded through Ollama

## Setup on Windows

1. Install Ollama from https://ollama.com/.
2. Open PowerShell or Command Prompt and download the model:

   ```powershell
   ollama pull phi3
   ```

3. In the project folder, install the Python dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. Start the chatbot:

   ```powershell
   py app.py
   ```

5. Open the local Gradio URL shown in the terminal (usually `http://127.0.0.1:7860`).

If Ollama is not already running, open the Ollama application or run `ollama serve` in a separate terminal.

## Setup on macOS or Linux

Install Python and Ollama, then run:

```bash
ollama pull phi3
python3 -m pip install -r requirements.txt
python3 app.py
```

Open the local Gradio URL printed in the terminal.

## Project files

- `app.py` — chatbot application
- `requirements.txt` — Python dependencies
- `chat_bot.ipynb` — original Google Colab notebook

## Important notes

- The application expects Ollama to be available at `http://127.0.0.1:11434`.
- The model runs on the computer where Ollama is installed. Running this application locally is different from running the notebook in Google Colab.
- The notebook includes Colab-specific installation and testing cells. Those cells are not needed to run `app.py` locally.
- This app does not need a cloud AI API key for local inference.
