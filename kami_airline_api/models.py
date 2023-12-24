from django.db import models

''' Just suppose in case we need to check airplane does exist'''
class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'airplane'