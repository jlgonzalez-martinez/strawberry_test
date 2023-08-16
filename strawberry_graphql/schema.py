import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension

from .queries import SchoolQueries

strawberry_schema = strawberry.Schema(
    query=SchoolQueries,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
