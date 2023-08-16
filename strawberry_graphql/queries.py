from typing import List

import strawberry as gql
from strawberry_django import connection
from strawberry_django.relay import ListConnectionWithTotalCount

from school.models import School
from strawberry_graphql.types import SchoolType


@gql.type
class SchoolQueries:
    """Queries for Schools."""

    @connection(ListConnectionWithTotalCount[SchoolType])
    def schools(
        self,
        info,
    ) -> List[School]:
        """Resolver to get the schools."""
        return School.objects.all()
