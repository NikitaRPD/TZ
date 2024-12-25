from dataclasses import dataclass

from src.infra.postgres.uow import PostgresUnitOfWork


@dataclass(slots=True)
class BaseController:
    """
    A controller class that delegates work to services, manages roles, and aggregates the response.
    """

    uow: PostgresUnitOfWork
