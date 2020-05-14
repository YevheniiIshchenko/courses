from django.db import models


# Create your models here.
class Group(models.Model):
    facult = models.CharField(max_length=64)
    spec = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField(max_length=64)
    number_of_students = models.PositiveSmallIntegerField(max_length=64)

    @property
    def code_of_group(self):
        return f'{self.facult} {self.spec}-{self.year}'
