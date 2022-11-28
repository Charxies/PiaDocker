from django.db import models


class Empleado(models.Model):
    objects = None
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    epos = models.CharField(max_length=45)
    econtact = models.IntegerField()
    class Meta:
        db_table = "empleado"
