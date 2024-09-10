import argparse
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from datetime import datetime

# Define a simplified prompt template
PROMPT_TEMPLATE = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Cutting Knowledge Date: December 2023
Today Date: {current_date}

You are a helpful assistant. Respond to the user's input directly and concisely.<|eot_id|>
<|start_header_id|>user<|end_header_id|>
{human_input}<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

def get_current_date():
    return datetime.now().strftime("%d %B %Y")

def setup_llm(api_base):
    return OpenAI(
        model_name="ws/models/Meta-Llama-3.1-70B-Instruct",
        openai_api_key="",
        base_url=api_base,
        temperature=0.7,
    )

def setup_chain(llm):
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["current_date", "human_input"]
    )
    return prompt | llm

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError as e:
        print(f"Error reading file: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="AI Command Line Tool")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-p", "--prompt", type=str, help="The prompt for the AI")
    input_group.add_argument("-f", "--file", type=str, help="Path to a text file containing the prompt")
    parser.add_argument("--api_base", type=str, default="http://0.0.0.0:8000/v1", help="The API base URL")
    args = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' does not exist.")
            exit(1)
        human_input = read_file(args.file)
    else:
        human_input = args.prompt

    llm = setup_llm(args.api_base)
    chain = setup_chain(llm)

    result = chain.invoke({
        "current_date": get_current_date(),
        "human_input": human_input
    })

    print(result)

if __name__ == "__main__":
    main()