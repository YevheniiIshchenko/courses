from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    stupen = models.CharField(max_length=64)
    isCurator = models.BooleanField

    @property
    def full_name(self):
        return f'{self.stupen} {self.first_name} {self.last_name} '


class Logger(models.Model):
    method = models.CharField(max_length=256, default='')
    path = models.CharField(max_length=256, default='')
    execution_time = models.FloatField()
    created = models.CharField(max_length=256, default='')

    def info(self):
        return f'{self.method} | {self.path} | {self.execution_time}sec | {self.created}'

    def __str__(self):
        return self.info()
