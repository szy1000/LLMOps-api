# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/16 23:52
@Author     : jack_shen
@File       : exception.py
@Description: 
"""
from dataclasses import dataclass, field
from typing import Any
from pkg.response import HttpCode


class CustomException(Exception):
    """自定义异常信息"""
    code: HttpCode = HttpCode.FAIl
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """通用失败异常"""
    pass


class NotFoundException(CustomException):
    """未找到数据异常"""
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    code = HttpCode.FORBIDDEN


class ValidationException(CustomException):
    code = HttpCode.VALIDATION_ERROR
