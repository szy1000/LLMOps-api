# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/15 21:52
@Author     : jack_shen
@File       : app_schema.py
@Description: 
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionsReq(FlaskForm):
    query = StringField('query', validators=[
        DataRequired(message='query is required'),
        Length(max=2000, message='query is too long')
    ])
