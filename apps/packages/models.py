from django.db import models

# Create your models here.
class PackChildFollow(models.Model):
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=150, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    autogenerado = models.CharField(max_length=40, blank=True, null=True)
    edad_mes = models.IntegerField(blank=True, null=True)
    ctrl1rn = models.DateField(blank=True, null=True)
    ctrl2rn = models.DateField(blank=True, null=True)
    ctrl3rn = models.DateField(blank=True, null=True)
    ctrl4rn = models.DateField(blank=True, null=True)
    cred1 = models.DateField(blank=True, null=True)
    cred2 = models.DateField(blank=True, null=True)
    neumo2 = models.DateField(blank=True, null=True)
    rota2 = models.DateField(blank=True, null=True)
    polio2 = models.DateField(blank=True, null=True)
    penta2 = models.DateField(blank=True, null=True)
    cred3 = models.DateField(blank=True, null=True)
    cred4 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    neumo4 = models.DateField(blank=True, null=True)
    rota4 = models.DateField(blank=True, null=True)
    penta4 = models.DateField(blank=True, null=True)
    polio4 = models.DateField(blank=True, null=True)
    cred5 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    cred6 = models.DateField(blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    dxAnemia = models.DateField(blank=True, null=True)
    suple6 = models.DateField(blank=True, null=True)
    polio6 = models.DateField(blank=True, null=True)
    penta6 = models.DateField(blank=True, null=True)
    cred7 = models.DateField(blank=True, null=True)
    suple7 = models.DateField(blank=True, null=True)
    cred8 = models.DateField(blank=True, null=True)
    suple8 = models.DateField(blank=True, null=True)
    cred9 = models.DateField(blank=True, null=True)
    suple9 = models.DateField(blank=True, null=True)
    cred10 = models.DateField(blank=True, null=True)
    suple10 = models.DateField(blank=True, null=True)
    cred11 = models.DateField(blank=True, null=True)
    suple11 = models.DateField(blank=True, null=True)
    eval_oral = models.DateField(blank=True, null=True)
    nutricion6 = models.DateField(blank=True, null=True)
    nutricion7 = models.DateField(blank=True, null=True)
    nutricion8 = models.DateField(blank=True, null=True)
    nutricion9 = models.DateField(blank=True, null=True)
    nutricion10 = models.DateField(blank=True, null=True)
    nutricion11 = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    pn = models.IntegerField(blank=True, null=True)
    dif1 = models.IntegerField(blank=True, null=True)
    dif2 = models.IntegerField(blank=True, null=True)
    dif3 = models.IntegerField(blank=True, null=True)
    dif4 = models.IntegerField(blank=True, null=True)
    dif5 = models.IntegerField(blank=True, null=True)
    dif6 = models.IntegerField(blank=True, null=True)
    dif7 = models.IntegerField(blank=True, null=True)
    dif8 = models.IntegerField(blank=True, null=True)
    dif9 = models.IntegerField(blank=True, null=True)
    dif10 = models.IntegerField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    num_rn = models.IntegerField(blank=True, null=True)
    num_cred = models.IntegerField(blank=True, null=True)
    num_vac = models.IntegerField(blank=True, null=True)
    num_suple = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_prov, self.cod_dist, self.cod_eess,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.autogenerado, self.edad_mes, self.ctrl1rn, self.ctrl2rn, self.ctrl3rn, self.ctrl4rn,\
               self.cred1, self.cred2, self.neumo2, self.rota2, self.polio2, self.penta2, self.cred3, self.cred4,\
               self.suple4, self.neumo4, self.rota4, self.penta4, self.polio4, self.cred5, self.suple5, self.cred6, \
               self.tmz, self.dxAnemia, self.suple6, self.polio6, self.penta6, self.cred7, self.suple7, self.cred8, \
               self.suple8, self.cred9, self.suple9, self.cred10, self.suple10, self.cred11, self.suple11, self.eval_oral, \
                self.nutricion6, self.nutricion7, self.nutricion8, self.nutricion9, self.nutricion10, self.nutricion11, self.programa, self.pn, \
               self.dif1, self.dif2, self.dif3, self.dif4, self.dif5, self.dif6, self.dif7, self.dif8, self.dif9, self.dif10, self.num, self.num_rn, self.num_cred, self.num_vac, self.num_suple, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento)


class PregnantFollow(models.Model):
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    autogenerado = models.CharField(max_length=60, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=200, blank=True, null=True)
    visit1 = models.DateField(blank=True, null=True)
    visit2 = models.DateField(blank=True, null=True)
    visit3 = models.DateField(blank=True, null=True)
    bacteruria = models.DateField(blank=True, null=True)
    sifilis = models.DateField(blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    vih = models.DateField(blank=True, null=True)
    perf_obst = models.DateField(blank=True, null=True)
    ctrl1 = models.DateField(blank=True, null=True)
    ctrl2 = models.DateField(blank=True, null=True)
    ctrl3 = models.DateField(blank=True, null=True)
    ctrl4 = models.DateField(blank=True, null=True)
    ctrl5 = models.DateField(blank=True, null=True)
    ctrl6 = models.DateField(blank=True, null=True)
    ctrl7 = models.DateField(blank=True, null=True)
    ctrl8 = models.DateField(blank=True, null=True)
    ctrl9 = models.DateField(blank=True, null=True)
    ctrl10 = models.DateField(blank=True, null=True)
    ctrl11 = models.DateField(blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    suple3 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.establecimiento,\
               self.documento, self.ape_nombres, self.autogenerado, self.documento, self.ape_nombres, self.bacteruria,\
               self.sifilis, self.tmz, self.vih, self.perf_obst, self.ctrl1, self.ctrl2, self.ctrl3, self.ctrl4, self.ctrl5,\
               self.ctrl6, self.ctrl7, self.ctrl8, self.ctrl9, self.ctrl10, self.ctrl11, self.suple1, self.suple2, self.suple3,\
               self.suple4, self.suple5, self.visit1, self.visit2, self.visit3, self.den,self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento)

