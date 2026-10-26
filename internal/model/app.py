# -*- coding: utf-8 -*-
"""
@Time       : 2026/10/22 19:28
@Author     : jack_shen
@File       : app.py
@Description: 
"""
import datetime
import uuid

from internal.extension.database_extension import db

from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    PrimaryKeyConstraint,
    DateTime,
    Index
)


class App(db.Model):
    __tablename__ = 'app'
    __table_args__ = (
        # 主键
        PrimaryKeyConstraint("id", name="pk_app_id"),
        # 索引
        Index("idx_app_account_id", "account_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    # updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    # created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    # def to_dict(self):
    #     return {
    #         "id": str(self.id),
    #         "account_id": str(self.account_id),
    #         "name": self.name,
    #         "icon": self.icon,
    #         "description": self.description,
    #         "updated_at": self.updated_at.isoformat() if self.updated_at else None,
    #         "created_at": self.created_at.isoformat() if self.created_at else None,
    #     }
