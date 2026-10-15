# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/15 22:58
@Author     : jack_shen
@File       : http_code.py
@Description: 
"""

from enum import Enum


class HttpCode(str, Enum):
    SUCCESS = "Success"  # 成功
    FAIl = "Fail"  # 失败
    NOT_FOUND = "not_found"  # 未找到
    FORBIDDEN = "forbidden"  # 无权限
    UNAUTHORIZED = "unauthorized"  # 未授权
    VALIDATION_ERROR = "validation_error"  # 数据验证错误
