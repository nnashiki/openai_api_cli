import os

import openai
from dotenv import load_dotenv
load_dotenv()

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]


def chat(message) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0]["message"]["content"].strip()
