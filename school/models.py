from django.db import models


class School(models.Model):
    """School model."""

    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    """Career model."""

    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    """Student model."""

    nia = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE, related_name="student"
    )

    def __str__(self):
        return self.nia
