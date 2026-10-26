import os

from flask import Flask

from internal.router import Router
from config import Config

from internal.exception import CustomException
from pkg.response import Response, json, HttpCode, message
from flask_sqlalchemy import SQLAlchemy
from internal.model import App


class Http(Flask):
    """http 服务引擎"""

    # args 非命名参数
    # **kwargs 命名参数
    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 2.初始化应用配置
        self.config.from_object(conf)

        # 3.注册应用路由
        self.register_error_handler(Exception, self._register_error_handler)

        # 4.初始化flask扩展开
        db.init_app(self)

        with self.app_context():
            # _ = App()
            db.create_all()

        # 5.注册路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        print('异常', error)
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                # data=error.data if error.data else {},
                data=error.data if error.data is not None else {},
            ))

        if self.debug or os.getenv('FLASK_ENV') == 'development':
            raise error
        return json(Response(
            code=HttpCode.FAIl,
            message=str(error),
            data={},
        ))
