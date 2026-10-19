# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/19 09:10
@Author     : jack_shen
@File       : test_app_handler.py
@Description: 
"""
import pytest
from pkg.response import HttpCode


class TestAppHandler:

    @pytest.mark.parametrize("query", [None, "你好"])
    def test_app_handler(self, query, client):
        resp = client.post('/app/completion', json={"query": query, })
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get('code') == HttpCode.VALIDATION_ERROR
        else:
            assert resp.json.get('code') == HttpCode.SUCCESS
            # assert 1 == 1
        print('响应内容', resp.json)
