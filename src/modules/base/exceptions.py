from dataclasses import dataclass


@dataclass(kw_only=True)
class AppException(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass(kw_only=True)
class NotFoundException(AppException):
    message: str = "Not found"
