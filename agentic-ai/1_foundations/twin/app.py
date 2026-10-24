import os
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(dotenv_path=PROJECT_ROOT / ".env", override=False)

if __package__:
    from .context import TWIN_SYSTEM_PROMPT
    from .style import CSS, EXAMPLES, JS
    from .tools import handle_tool_calls_manual_if, tools
else:
    from context import TWIN_SYSTEM_PROMPT
    from style import CSS, EXAMPLES, JS
    from tools import handle_tool_calls_manual_if, tools

MODEL_NAME = "gemini-3.6-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY1") or os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
if not gemini_api_key:
    raise RuntimeError("Set GEMINI_API_KEY1 or GEMINI_API_KEY in the project .env file.")
if not gemini_base_url:
    raise RuntimeError("Set GEMINI_BASE_URL in the project .env file.")

gemini = OpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = gemini.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    while response.choices[0].finish_reason == "tool_calls":
        assistant_message = response.choices[0].message
        tool_calls = assistant_message.tool_calls or []
        if not tool_calls:
            raise RuntimeError("The model indicated a tool call but returned no tool calls.")

        messages.append(assistant_message.model_dump(exclude_none=True))
        results = handle_tool_calls_manual_if(tool_calls)
        messages.extend(results)
        response = gemini.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
        )
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        examples=EXAMPLES,
        title="Karan Pratap Singh | Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(
            show_label=False,
            elem_id="karan-chatbot",
        ),
        textbox=gr.Textbox(
            placeholder="Message Karan...",
            elem_id="karan-input",
        ),
    ).launch(inbrowser=True, css=CSS, js=JS, theme=gr.themes.Base())