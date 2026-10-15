# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/15 23:01
@Author     : jack_shen
@File       : response.py
@Description: 
"""

from dataclasses import dataclass, field, asdict
from flask import jsonify
from .http_code import HttpCode
from typing import Any


@dataclass
class Response:
    "基础HTTP接口响应"

    code: int = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data), 200


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAIl, message="", data=data))


def validation_error_json(errors: dict = None):
    first_keys = next(iter(errors))
    if first_keys is not None:
        msg = errors.get(first_keys)[0]
    else:
        msg = ''
    return json(Response(code=HttpCode.VALIDATION_ERROR, message="", data=errors))


def message(code: HttpCode = None, msg: str = ''):
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ''):
    return message(HttpCode.SUCCESS, msg)


def fail_message(msg: str = ''):
    return message(HttpCode.FAIL, msg)


def not_found_message(msg: str = ''):
    return message(HttpCode.NOT_FOUND, msg)


def unauthorized_message(msg: str = ''):
    return message(HttpCode.UNAUTHORIZED, msg)


def forbidden_message(msg: str = ''):
    return message(HttpCode.FORBIDDEN, msg)
