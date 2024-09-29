import together
import os
from dotenv import load_dotenv

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
    print(completion.choices[0].message.content)