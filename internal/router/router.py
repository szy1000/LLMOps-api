from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    app_handler: AppHandler

    #
    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1.创建一个蓝图
        bp = Blueprint("router", __name__, url_prefix="/")

        # 2.将Url与对应的控制器方法绑定
        # app_handler = AppHandler
        # bp.add_url_rule('/ping', view_func=app_handler.ping, methods=['GET'])
        bp.add_url_rule('/ping', view_func=self.app_handler.ping, methods=['GET'])

        app.register_blueprint(bp)
