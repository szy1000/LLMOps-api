# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/19 09:51
@Author     : jack_shen
@File       : conftest.py
@Description: 
"""

import pytest
from app.http.app import app


@pytest.fixture
def client():
    """"获取flask的测试应用"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
