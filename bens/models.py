from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator



class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    id = models.CharField(max_length=20, primary_key=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("bens:list_by_category", kwargs={"slug": self.slug})




class Product(TimeStampedModel):
    categoria = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    codbem = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0, unique=True)
    descricao = models.CharField(max_length=3000, blank=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    setor = models.CharField(max_length=255, blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="codbem")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    
    is_available = models.BooleanField(default=True)
    
    

    objects = models.Manager()
    available = AvailableManager()


    class Meta:
        ordering = ("slug",)
        verbose_name = "imobilizado"
        verbose_name_plural = "imobilizados"

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("bens:detail", kwargs={"slug": self.slug})

Product.objects.last
