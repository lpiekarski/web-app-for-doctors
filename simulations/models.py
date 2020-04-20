from django.db import models
from django.contrib.auth.models import User
from protocols.models import Protocol


class InitialTumor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to='tumors/')  # TODO: add validation check for correct tumor file

    class Meta:
        verbose_name = 'Initial Tumor'

    def __str__(self):
        return self.name


class Simulation(models.Model):
    name = models.CharField(max_length=100, blank=False)  # TODO: add validation for correct protocol
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simulations', null=False)
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE, related_name='simulations', null=False)
    description = models.TextField(null=False)
    time_duration = models.FloatField(null=False)

    class Meta:
        verbose_name = 'Tumor Simulation'

    def __str__(self):
        return self.name


class SimulationState(models.Model):
    simulation = models.ForeignKey(to='Simulation', on_delete=models.CASCADE, related_name='state', null=False)
    time = models.IntegerField(verbose_name='Time', null=False)
    _W = models.TextField(null=False)
    _CHO = models.TextField(null=False)
    _OX = models.TextField(null=False)
    _GI = models.TextField(null=False)
    _timeInRepair = models.TextField(null=False)
    _irradiation = models.TextField(null=False)
    _cellState = models.TextField(null=False)
    _cellCycle = models.TextField(null=False)
    _proliferationTime = models.TextField(null=False)
    _cycleChanged = models.TextField(null=False)
    _G1time = models.TextField(null=False)
    _Stime = models.TextField(null=False)
    _G2time = models.TextField(null=False)
    _Mtime = models.TextField(null=False)
    _Dtime = models.TextField(null=False)

    class Meta:
        verbose_name = 'Simulation State'