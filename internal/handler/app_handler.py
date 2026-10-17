import os

from flask import request, jsonify
from openai import OpenAI
from internal.schema.app_schema import CompletionsReq
from pkg.response import success_json, validation_error_json
from internal.exception import FailException


class AppHandler:

    def completion(self):
        # try:
        #     json_data = request.get_json()
        # except Exception as e:
        #     return jsonify({
        #         "status": "error",
        #         "code": 400,
        #         "msg": "JSON解析失败，请检查格式，使用双引号"
        #     }), 400
        req = CompletionsReq()
        if not req.validate():
            # return jsonify({
            #     "status": "error",
            #     "code": 200,
            #     "msg": req.errors
            # })
            # return req.errors, 200
            return validation_error_json(req.errors)
        # query = request.json.get("query")
        print(req.query.data)
        client = OpenAI()

        response = client.chat.completions.create(
            model='qwen3.7-plus',
            messages=[
                {"role": "system", "content": "你是一个AI助手，根据用户输入的信息进行反馈"},
                {"role": "user", "content": req.query.data}
            ]
        )
        content = response.choices[0].message.content
        return success_json({"content": content})

    def ping(self):
        raise FailException('数据异常')
        return "pong 12345！"
