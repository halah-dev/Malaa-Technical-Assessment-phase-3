""" Alert Rule Model """

from db.models.model_base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, String, DateTime
from datetime import datetime
import uuid


class AlertRule(Base):
    __tablename__ = "alert-rules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol = Column(String)
    name = Column(String)
    threshold_price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
