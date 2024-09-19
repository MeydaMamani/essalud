from django.db import models

# Create your models here.
class Departamento(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s' % (self.codigo, self.nombre)


class Provincia(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=60)
    parent= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre, self.parent

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre, self.parent)


class Distrito(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=50)
    prov= models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre, self.prov

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre, self.prov)


class Establecimiento(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=90)
    dist= models.ForeignKey(Distrito, on_delete=models.CASCADE, null=True, blank=True)
    prov= models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre, self.dist

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre, self.dist)

