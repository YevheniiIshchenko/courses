from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()

    def show_student(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def __str__(self):
        return self.show_student()
