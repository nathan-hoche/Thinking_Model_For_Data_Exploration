from ollama import chat
from colorama import Fore
import re

class LLMHandler:
    def __init__(self, model_name: str):
        self.model = model_name

    def get_history(self, query:str, system_prompt:str=None, history:list=None) -> list:
        res = [{'role': 'system_prompt', 'content': system_prompt}] if system_prompt else []

        if history:
            res.extend(history)
        res.append({'role': 'user', 'content': query})
        return res

    def ask(self, query:str, system_prompt:str=None, history:list=None, tools:list=None):
        stream = chat(
            model=self.model,
            messages=self.get_history(query, system_prompt, history),
            tools=tools,  # List your tool functions here
            stream=True
        )

        res = ""
        print(Fore.LIGHTBLACK_EX, end='')
        for chunk in stream:
            print(chunk.message.content, end='', flush=True)
            res += chunk.message.content
            if chunk.message.tool_calls:
                print(Fore.YELLOW + chunk.message.tool_calls + Fore.LIGHTBLACK_EX, end='')
        print(Fore.RESET)
        return re.sub(r'<think>.*?</think>', '', res, flags=re.DOTALL)