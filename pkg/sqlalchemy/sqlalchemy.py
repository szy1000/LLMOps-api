# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/26 21:57
@Author     : jack_shen
@File       : sqlalchemy.py
@Description:
"""

from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写Flask-SQLAlchemy核心类"""

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
