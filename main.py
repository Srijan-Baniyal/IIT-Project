import together
import os
import sys
import time
from dotenv import load_dotenv

def typing_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

load_dotenv()
samp = []
api_key = os.getenv("API_KEY")

client = together.Together(api_key=api_key)

for i in range(15):
    message=str(input(">>> "))
    samp.append(message)
    if message == "exit":
        break
    if ("previous" in message) and ("command" in message) and ("run" not in message):
        print("your last command was '{}'".format(samp[-2]))

    if ("previous" in message) and ("command" in message) and ("run" in message):
        message = samp[-2]
    
    completion=client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",messages=[{"role":"user","content":message}])
    typing_effect((completion.choices[0].message.content), 0.05)



