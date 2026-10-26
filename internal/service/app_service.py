# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/26 20:53
@Author     : jack_shen
@File       : app_service.py
@Description: 
"""

import uuid

from injector import inject
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from internal.model import App


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> App:
        # 1.创建模型的实体类
        app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的机器人")

        # 2. 将实体类添加到session会话中

        self.db.session.add(app)

        # 3.提交session会话
        self.db.session.commit()
        return app

    def query_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        app = self.query_app(id)
        app.name = 'jack shen'
        self.db.session.commit()
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        app = self.query_app(id)
        self.db.session.delete(app)
        self.db.session.commit()
        return app
