from shortuuidfield import ShortUUIDField

from django.db import models

class InputData(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.TextField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
