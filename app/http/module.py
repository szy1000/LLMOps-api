# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/19 10:51
@Author     : jack_shen
@File       : module.py
@Description: 
"""
from internal.extension.database_extension import db
from injector import Module, Binder
from flask_sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
