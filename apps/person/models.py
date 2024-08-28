# from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, AbstractBaseUser, BaseUserManager
# from apps.redes.models import Redes, Entity

class Person(models.Model):
    CHOICES_TYPE_SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    CHOICES_TYPE_DOC = (
        ('D', 'DNI'),
        ('CE', 'CARNET EXTRANJERIA')
    )

    # eid         = models.ForeignKey(Entity, on_delete=models.PROTECT)
    typedoc     = models.CharField(max_length=5, choices=CHOICES_TYPE_DOC)
    pdoc        = models.CharField(max_length=20)
    last_name0  = models.CharField(max_length=150)
    last_name1  = models.CharField(max_length=150)
    names       = models.CharField(max_length=150)
    birthday    = models.DateField(auto_now=False, auto_now_add=False,  null=True)
    sex         = models.CharField(max_length=1, choices=CHOICES_TYPE_SEX)
    pmail       = models.CharField(max_length=100, null=True)
    phone       = models.CharField(max_length=9, null=True)
    institution = models.CharField(max_length=100, null=True)

    user_create = models.CharField(max_length=50,null=True, blank=True)
    user_update = models.CharField(max_length=50, null=True,blank=True,)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.last_name0, self.last_name1, self.names,\
               self.pdoc, self.birthday, self.sex, self.pmail, self.institution

    def __str__(self):
        return '%s %s, %s' % (self.last_name0,self.last_name1, self.names )

    class Meta:
        unique_together = ('pdoc'),


class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico')
        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,  password=None):
        user = self.create_user(username,email, password=password )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    CHOICES_TYPE_CA = (
        ('DP', 'DEPARTAMENTO'),
        ('PR', 'PROVINCIA'),
        ('DS', 'DISTRITO'),
        ('CA', 'CENTRO ASISTENCIAL'),
    )

    username   = models.CharField(max_length=15, unique=True, db_index=True)
    email      = models.EmailField(max_length=255)
    is_active  = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)

    id_person  = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    type_ca    = models.CharField(max_length=2, choices=CHOICES_TYPE_CA)
    code_ca    = models.IntegerField(blank=True, null=True)
    # id_red     = models.ForeignKey(Redes, on_delete=models.CASCADE, null=True,blank=True)

    objects = UserProfileManager()

    def natural_key(self):
        return self.pk, self.username, self.id_person.pk

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Usuario de sistema'
        verbose_name_plural = 'Usuarios del sistema'

    def get_full_name(self):
        return '{0} {1}'.format(self.username)

    def get_short_name(self):
        return self.username
