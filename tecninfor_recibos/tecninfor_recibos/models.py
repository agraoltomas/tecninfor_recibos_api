# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'categoria'


class Empleados(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    cuil = models.CharField(primary_key=True, max_length=11)
    fecha_nacim = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria', blank=True, null=True)
    viandas = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'empleados'


class Fechas(models.Model):
    fecha = models.DateField()
    descr = models.CharField(max_length=200, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='user', blank=True, null=True)
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fechas'


class Liquidaciones(models.Model):
    periodo = models.IntegerField(primary_key=True)
    publica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liquidaciones'


class Login(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    salt = models.CharField(max_length=21, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    cuil = models.OneToOneField(Empleados, models.DO_NOTHING, db_column='cuil', primary_key=True)
    admin = models.IntegerField(blank=True, null=True)
    habilitado = models.IntegerField(blank=True, null=True)
    last_pwd_change = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class NivelFechas(models.Model):
    nivel = models.IntegerField(blank=True, null=True)
    descr = models.CharField(max_length=30, blank=True, null=True)
    habilitado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_fechas'


class Recibos(models.Model):
    cuil = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='cuil', blank=True, null=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)
    documento = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.ForeignKey('TipoLiquidacion', models.DO_NOTHING, db_column='tipo', blank=True, null=True)
    bytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos'
        unique_together = (('periodo', 'cuil', 'tipo'),)


class TipoLiquidacion(models.Model):
    uid = models.IntegerField(primary_key=True,unique=True, blank=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_liquidacion'
