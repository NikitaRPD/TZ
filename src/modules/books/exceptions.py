from dataclasses import dataclass, field
from uuid import UUID
from src.modules.base.exceptions import NotFoundException


@dataclass(kw_only=True)
class AuthorsNotFoundException(NotFoundException):
    missing_ids: list[UUID] = field(default_factory=list)
    message: str = "Authors not found"

    def __str__(self) -> str:
        if self.missing_ids:
            return f"{self.message}: {self.missing_ids}"
        return self.message
