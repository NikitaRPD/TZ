from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    metadata = MetaData()

    @classmethod
    @declared_attr
    def __mapper_args__(cls) -> dict[str, Any]:
        return {"eager_defaults": True}