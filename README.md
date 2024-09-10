# Local LLM Inference with vLLM and LangChain

This project demonstrates how to run Large Language Models (LLMs) locally using vLLM as the inference engine and LangChain as the frontend framework. It provides a flexible command-line interface for interacting with your local LLM.

## Setting Up the Environment

This project relies on two main components:

1. **vLLM**: An open-source library for fast LLM inference.
2. **LangChain**: A framework for developing applications powered by language models.

Ensure you have a compatible LLM model downloaded. You can use models from Hugging Face or other sources that are compatible with vLLM.

## Running the Local Server

To start the local inference server using vLLM, use the following command:

```
python -m vllm.entrypoints.openai.api_server \
    --model <path_to_model> \
    --trust-remote-code \
    --tensor-parallel-size 4 \
    --host 192.168.0.172 \
    --port 8000
```

Replace `<path_to_model>` with the path to your downloaded model.

Parameters explained:
- `--model`: Specifies the path to your LLM model.
- `--trust-remote-code`: Allows execution of remote code (use with trusted models only).
- `--tensor-parallel-size`: Sets the number of GPUs to use for tensor parallelism.
- `--host`: The IP address to bind the server to (use your machine's local IP).
- `--port`: The port number to run the server on.

Adjust these parameters based on your setup and requirements.

## Using the Inference Client

The `llm.py` script provides a command-line interface for interacting with your local LLM server.

### Basic Usage

To run an inference with a direct prompt:

```
python llm.py -p "Write a paragraph about the AI revolution."
```

To use a prompt from a file:

```
python llm.py -f /path/to/your/prompt_file.txt
```

### Advanced Options

- Specify a custom API base URL:
  ```
  python llm.py -p "Your prompt" --api_base "http://your-custom-url:8000/v1"
  ```

### Full Command-line Options

- `-p`, `--prompt`: Directly input a prompt for the AI.
- `-f`, `--file`: Specify a file containing the prompt.
- `--api_base`: Set a custom API base URL (default: `http://0.0.0.0:8000/v1`).
