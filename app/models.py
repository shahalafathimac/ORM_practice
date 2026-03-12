from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    credits = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    courses = models.ManyToManyField(
        Course,
        related_name="students"
    )

    joined_date = models.DateField()

    def __str__(self):
        return self.name