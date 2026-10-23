from openai import OpenAI
import os
from tools import tools, handle_tool_calls_manual_if
from style import CSS, EXAMPLES, JS
from context import TWIN_SYSTEM_PROMPT
from dotenv import load_dotenv
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)


MODEL_NAME = "gemini-3.6-flash"



gemini_api_key= os.getenv("GEMINI_API_KEY1")
gemini_base_url= os.getenv("GEMINI_BASE_URL")
gemini= OpenAI(api_key=gemini_api_key,base_url=gemini_base_url)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages=system+history+[{"role":"user", "content":message}]
    response=gemini.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools
    )
    while response.choices[0].finish_reason=="tool_calls":
        message= response.choices[0].message
        tool_Calls= message.tool_calls
        results= handle_tool_calls_manual_if(tool_Calls)
        messages.append(message)
        messages.extend(results)
        response=gemini.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools 
        )
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())