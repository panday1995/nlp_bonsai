import uuid
from enum import Enum

from config import ENGINE
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Schema(Enum):
    DESCRIP_BONSAI = "description_bonsai"
    DESCRIP_EXTERNAL = "description_external"
    SOURCE_EXTERNAL = "source_external"


# Setup model for sqlite table
class Correspondence(Base):
    __tablename__ = "correspondence"
    id = Column(
        String,
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    description_bonsai = Column(String)
    description_external = Column(String)
    source_external = Column(String)
