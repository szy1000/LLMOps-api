from flask import Flask

from internal.router import Router
from config import Config


class Http(Flask):
    """http 服务引擎"""

    # args 非命名参数
    # **kwargs 命名参数
    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # 注册应用路由
        router.register_router(self)
        self.config.from_object(conf)
