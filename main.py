import together
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = together.Together(api_key=api_key)

for i in range(15):
    message=str(input(">>> "))
    if message == "exit":
        break
    completion=client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",messages=[{"role":"user","content":message}])
    print(completion.choices[0].message.content)