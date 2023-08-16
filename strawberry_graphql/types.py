from typing import List

import strawberry_django as gql
from strawberry import relay, auto
from strawberry_django.relay import ListConnectionWithTotalCount

from school.models import Career, Student, School


@gql.type(Career)
class CareerType(relay.Node):
    title: auto


@gql.type(Student)
class StudentType(relay.Node):
    name: auto
    nia: auto
    career: "CareerType"

    @gql.field
    def upper_name(self) -> str:
        """Return the name in uppercase."""
        return self.name.upper()


@gql.type(School)
class SchoolType(relay.Node):
    name: auto
    students: List[StudentType]
    # students: ListConnectionWithTotalCount[StudentType] = gql.connection(
    #     prefetch_related="students"
    # )
