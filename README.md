# Local ChatStream: ChatGPT-Style Interface with Ollama

This project provides a comprehensive, step-by-step approach to building a ChatGPT-style chatbot using **Streamlit** for the user interface and leveraging local Large Language Models (LLMs) via **Ollama**.

By using Ollama, this chatbot runs entirely on your local machine—meaning **zero API costs**, no data leaving your device, and total privacy.


## Libraries Used

* **Streamlit**: For building the interactive, web-based chat interface.
* **OpenAI Python Library**: Used to connect to Ollama via its OpenAI-compatible API bridge.
* **Ollama**: The backend engine responsible for running and serving the LLMs locally.


## Getting Started

### 1. Install Ollama

Download and install Ollama from [ollama.com](https://ollama.com). Once installed, ensure the Ollama application is running in your system tray.

### 2. Pull Your Models

Open your terminal and download the models used in this project:

```bash
ollama pull llama3:latest
ollama pull gemma3:1b

```

### 3. Install Python Dependencies

Install the required packages using pip:

```bash
pip install streamlit openai

```


## Configuration & Setup

The chatbot is pre-configured to point to your local machine. Unlike the official OpenAI API, you do **not** need a paid subscription or a real API key.

* **Base URL:** `http://localhost:11434/v1`
* **API Key:** `ollama` (This acts as a placeholder; Ollama does not require a real key).


## Key Features

* **Conversational Memory**: The bot maintains the context of your conversation throughout the session.
* **Adjustable Parameters**:
* **Model Selection**: Seamlessly switch between `llama3:latest` and `gemma3:1b`.
* **Temperature**: Adjust the slider to control "creativity" (0.0 for focused, 2.0 for creative).
* **Max Tokens**: Limit the response length to manage performance and speed.


* **Real-time Streaming**: Responses appear word-by-word, providing a modern AI experience.



## Usage

To launch your chatbot, navigate to your project directory in the terminal and run:

```bash
streamlit run app.py

```


### Project Pro-Tip

If you want to use other models, simply use `ollama pull <model_name>` in your terminal and add that name to the `selected_model` list in your `app.py` file.

