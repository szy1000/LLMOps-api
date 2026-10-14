import os

from flask import request
from openai import OpenAI


class AppHandler:

    def completion(self):
        query = request.json.get("query")

        client = OpenAI()

        response = client.chat.completions.create(
            model='qwen3.7-plus',
            messages=[
                {"role": "system", "content": "你是一个AI助手，根据用户输入的信息进行反馈"},
                {"role": "user", "content": query}
            ]
        )

        return response.choices[0].message.content

    def ping(self):
        return "pong 12345！"
