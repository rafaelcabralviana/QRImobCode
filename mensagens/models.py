from django.db import models
from bens.models import Product
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
# Create your models here.


class Erro(TimeStampedModel):
    bem = models.ForeignKey(
        Product, related_name="erro", on_delete=models.CASCADE
    )
    email = models.EmailField(max_length=250)

    mensagem = models.TextField(max_length=3000)

    image = models.ImageField(upload_to="erro/%Y/%m/%d", blank=True)

    slug = AutoSlugField(unique=True, always_update=False, populate_from="bem")

    class Meta:
        ordering = ("bem",)
        verbose_name = "erro"
        verbose_name_plural = "erros"


class Uso(TimeStampedModel):
    bem = models.ForeignKey(
        Product, related_name="uso", on_delete=models.CASCADE
    )
    email = models.EmailField(max_length=250)

    motivo = models.CharField(max_length=250)

    mensagem = models.TextField(max_length=3000)

    image = models.ImageField(upload_to="uso/%Y/%m/%d", blank=True)

    slug = AutoSlugField(unique=True, always_update=False, populate_from="bem")

    class Meta:
        ordering = ("bem",)
        verbose_name = "solicitação"
        verbose_name_plural = "solicitações"