import together
import os
import sys
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import colorama
import sys
import time

RED = "\x1b[1;31;40m"
GREEN = " \x1b[32m"
YELLOW = "\x1b[33m"

console = Console()
load_dotenv()
api_key = os.getenv("API_KEY")
client = together.Together(api_key=api_key)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def hook(tp, *args) -> None:
    if tp is KeyboardInterrupt:
        print(colorama.Fore.RED)
        exit()


def colourized_input(text: str, color: str) -> (str | None):
    while True:
        try:
            sys.excepthook = hook
            inp = input(text + color).strip()
            print(colorama.Fore.RESET, end="", flush=True)
            if not inp:
                raise ValueError("Input cannot be empty")
            return inp
        except ValueError as e:
            print(f"{color}{e}{colorama.Fore.RESET}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break


def typing_effect(num: int, text: str, style: str) -> None:
    console = Console()
    try:
        for char in text:
            console.print(char, style=style, end="")
            time.sleep(num)
        console.print()
    except Exception as e:
        console.print(f"An error occurred: {e}")


# def format_message(message: str) -> str:
#     message = message.replace("**", "[bold]").replace("**", "[/bold]", 1)
#     message = message.replace("`", "[i]").replace("`", "[/i]", 1)
#     return message

def render_markdown(text):
    console = Console()
    markdown = Markdown(text)
    console.print(markdown)

def Main_Loop() -> None:
    i = 0
    while i < 15:
        message = str(colourized_input(
            f"{RED}>>>>>>>>>>>> ", colorama.Fore.GREEN))
        if message == "exit":
            break
        if message == "clear":
            clear()
            message = str(colourized_input(
                f"{RED}>>> ", colorama.Fore.GREEN))
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages=[{"role": "user", "content": message}])
        # formatted_message = format_message(
        #     completion.choices[0].message.content)
        # typing_effect(0.05, formatted_message,
        #               style="bold blue")
        render_markdown(completion.choices[0].message.content)
        i += 1


Main_Loop()
