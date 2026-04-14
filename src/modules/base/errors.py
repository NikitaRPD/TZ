from dataclasses import dataclass


@dataclass(kw_only=True)
class AppError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass(kw_only=True)
class NotFoundError(AppError):
    message: str = "Not found"
