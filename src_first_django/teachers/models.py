from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    stupen = models.CharField(max_length=64)
    isCurator = models.BooleanField

    @property
    def full_name(self):
        return f'{self.stupen} {self.first_name} {self.last_name} '
