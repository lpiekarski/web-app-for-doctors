from django.db import models


class InitialTumor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to='tumors/')  # TODO: add validation check for correct tumor file