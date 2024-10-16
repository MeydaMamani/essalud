from django.db import models

# Create your models here.
class Anemia(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=5, blank=True, null=True)
    cod_prov = models.CharField(max_length=5, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=8, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=5, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=200, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    edad_mes = models.IntegerField(blank=True, null=True)
    dosaje1 = models.DateField(blank=True, null=True)
    result1 = models.CharField(max_length=200, blank=True, null=True)
    dosaje2 = models.DateField(blank=True, null=True)
    result2 = models.CharField(max_length=200, blank=True, null=True)
    dx_anemia1 = models.DateField(blank=True, null=True)
    dx_anemia2 = models.DateField(blank=True, null=True)
    nutricion6 = models.DateField(blank=True, null=True)
    nutricion7 = models.DateField(blank=True, null=True)
    nutricion8 = models.DateField(blank=True, null=True)
    nutricion9 = models.DateField(blank=True, null=True)
    nutricion10 = models.DateField(blank=True, null=True)
    nutricion11 = models.DateField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    enf6 = models.DateField(blank=True, null=True)
    enf7 = models.DateField(blank=True, null=True)
    enf8 = models.DateField(blank=True, null=True)
    enf9 = models.DateField(blank=True, null=True)
    enf10 = models.DateField(blank=True, null=True)
    enf11 = models.DateField(blank=True, null=True)
    grupo_edad= models.CharField(max_length=100, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_dep, self.cod_prov, self.provincia, self.cod_dist,\
               self.distrito, self.cod_eess, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.edad_mes, self.dosaje1, self.result1, self.dosaje2, self.result2, self.dx_anemia1,\
               self.dx_anemia2, self.nutricion6, self.nutricion7, self.nutricion8, self.nutricion9, self.nutricion10, self.cred3, self.cred4,\
               self.nutricion11, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento)


class VaccinexPat(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    fec_atencion = models.DateField(blank=True, null=True)
    id_eess = models.IntegerField(blank=True, null=True)
    eess = models.CharField(max_length=500, blank=True, null=True)
    tipo_doc = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    lab = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=1500, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    tipo_edad = models.CharField(max_length=5, blank=True, null=True)
    anio_act= models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.fec_atencion, self.id_eess, self.tipo_doc, self.documento,\
               self.fec_nac, self.codigo, self.lab, self.descripcion, self.edad, self.tipo_edad, self.anio_act


class Inmunization(models.Model):
    cod_dep = models.IntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=200, blank=True, null=True)
    cod_prov = models.CharField(max_length=5, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    cod_dist = models.IntegerField(blank=True, null=True)
    distrito = models.CharField(max_length=200, blank=True, null=True)
    cod_eess = models.IntegerField(blank=True, null=True)
    eess = models.CharField(max_length=200, blank=True, null=True)
    autogenerado = models.CharField(max_length=50, blank=True, null=True)
    documento = models.CharField(max_length=25, blank=True, null=True)
    paciente = models.CharField(max_length=300, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    hvb = models.DateField(blank=True, null=True)
    bcg = models.DateField(blank=True, null=True)
    rota2m = models.DateField(blank=True, null=True)
    apo2m = models.DateField(blank=True, null=True)
    penta2m = models.DateField(blank=True, null=True)
    neumo2m = models.DateField(blank=True, null=True)
    rota4m = models.DateField(blank=True, null=True)
    apo4m = models.DateField(blank=True, null=True)
    penta4m = models.DateField(blank=True, null=True)
    neumo4m = models.DateField(blank=True, null=True)
    apo6m = models.DateField(blank=True, null=True)
    penta6m = models.DateField(blank=True, null=True)
    neumo6m = models.DateField(blank=True, null=True)
    infl6m = models.DateField(blank=True, null=True)
    infl7m = models.DateField(blank=True, null=True)
    spr1 = models.DateField(blank=True, null=True)
    varicela = models.DateField(blank=True, null=True)
    hiv = models.DateField(blank=True, null=True)
    ama = models.DateField(blank=True, null=True)
    spr2 = models.DateField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.cod_dep, self.departamento, self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, \
                self.autogenerado, self.documento, self.paciente, self.edad, self.fec_nac, self.hvb, self.bcg, self.rota2m, self.apo2m, self.penta2m, \
                self.neumo2m, self.rota4m, self.apo4m, self.penta4m, self.neumo4m, self.apo6m, self.penta6m, self.neumo6m, self.infl6m, self.infl7m, \
                self.spr1, self.varicela, self.hiv, self.ama, self.spr2
