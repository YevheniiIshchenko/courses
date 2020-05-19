from django.db import models


# Create your models here.
class Group(models.Model):
    facult = models.CharField(max_length=64)
    spec = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField(max_length=64)
    number_of_students = models.PositiveSmallIntegerField(max_length=64)

    @property
    def code_of_group(self):
        return f'{str(self.facult)[0]}{str(self.spec)[0]}-{self.year}'

    def __str__(self):
        return f'{str(self.facult)} {str(self.spec)} {self.year}'
