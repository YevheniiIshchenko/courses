from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()

    @property
    def show_student(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'


class Group(models.Model):
    facult = models.CharField(max_length=64)
    spec = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField(max_length=64)
    number_of_students = models.PositiveSmallIntegerField(max_length=64)

    @property
    def code_of_group(self):
        return f'{self.facult[0]}{self.spec[0]}-{self.year}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    stupen = models.CharField(max_length=64)
    isCurator = models.BooleanField

    @property
    def full_name(self):
        return f'{self.stupen} {self.first_name} {self.last_name} '