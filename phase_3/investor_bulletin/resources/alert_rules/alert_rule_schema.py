""" Alert Rule Schema """

"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel
from resources.common.symbols_schema import Symbols
from datetime import datetime
from uuid import UUID


class AlertRuleCreate(BaseModel):
    symbol: Symbols
    name: str
    threshold_price: float


class AlertRuleData(BaseModel):
    id: UUID
    symbol: Symbols
    name: str
    threshold_price: float
    created_at: datetime
    status: bool
