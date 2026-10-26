import os

from flask import request, jsonify
from openai import OpenAI
from internal.schema.app_schema import CompletionsReq
from pkg.response import success_json, validation_error_json, success_message
from internal.exception import FailException, NotFoundException
from internal.service import AppService
from injector import inject
from dataclasses import dataclass
import uuid


@inject
@dataclass
class AppHandler:
    app_service: AppService

    def create_app(self):
        """调用服务创建APP记录"""

        app = self.app_service.create_app()
        return success_message(f"应用已经创建，id:{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.query_app(id)
        if app is None:
            raise NotFoundException("应用不存在")
        # return success_json(app)
        return success_message(f"应用已经获取，name:{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用名称已经更改， name:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用名称已经删除， name: {app.name},id:{app.id}")

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
