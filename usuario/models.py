from django.db import models
from django.contrib.auth.models import User


class ModelProfile(models.Model):
    CIDADES_CHOICES = (
        ("PF", "PASSO FUNDO"),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # # Dados pessoais
    foto = models.ImageField(upload_to="profile", null=True, blank=True)
    cidade = models.CharField(max_length=50, choices=CIDADES_CHOICES, default="")
    bairro = models.CharField(max_length=50, default="")
    data_nascimento = models.DateField(null=True, blank=True)

    # # Configurações
    desenvolvedor = models.BooleanField(default=False)
    status = models.BooleanField(default=True, blank=False, null=False)

    # # Media
    quantidade_posts = models.IntegerField(default=0, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True, default="")
    twitter = models.URLField(null=True, blank=True, default="")
    instagram = models.URLField(null=True, blank=True, default="")
    linkedin = models.URLField(null=True, blank=True, default="")
    website = models.URLField(null=True, blank=True, default="")

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.usuario.username

    def get_full_name(self):
        return self.usuario.first_name + " " + self.usuario.last_name

    def get_dict_profile(self):
        return {'usuario': self.usuario,
                'foto': self.foto,
                'cidade': self.cidade,
                'bairro': self.bairro,
                'data_nascimento': self.data_nascimento,
                'facebook': self.facebook,
                'twitter': self.twitter,
                'instagram': self.instagram,
                'linkedin': self.linkedin,
                'website': self.website}

    def get_dict_user(self):
        return {'email': self.usuario.email,
                'first_name': self.usuario.first_name,
                'last_name': self.usuario.last_name}