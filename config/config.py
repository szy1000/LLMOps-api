# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/15 22:03
@Author     : jack_shen
@File       : config.py
@Description: 
"""
import os
from .default_config import DEFAULT_CONFIG


def _get_env(key: str):
    # return os.environ.get(key)
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str):
    value = _get_env(key)
    return value.lower() == "true" if value is not None else False


class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_bool_env('WTF_CSRF_ENABLE')

        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIOS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
