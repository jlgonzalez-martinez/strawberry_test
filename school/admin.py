from django.contrib import admin

from school.models import School, Career, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
