from ollama import chat
from colorama import Fore

class LLMHandler:
    def __init__(self, model_name: str):
        self.model = model_name

    def get_history(self, query:str, history:list=None) -> list:
        res = history or []

        res.append({'role': 'user', 'content': query})
        return res

    def ask(self, query:str, history:list=None, tools:list=None):
        stream = chat(
            model=self.model,
            messages=self.get_history(query, history),
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
        print(Fore.RESET, end='')