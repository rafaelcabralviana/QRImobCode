from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
import datetime


#diretorio- arquivo foto
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.codigo, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
#_____________________________


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

    codigo = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0, unique=True)
    descricao = models.CharField(max_length=3000, blank=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    setor = models.CharField(max_length=255, blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    responsavel = models.CharField(max_length=255, blank=True, null=True)
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="codigo")
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    
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
    
    def get_absolute_url_imagem(self):
        return reverse("bens:imagembem", kwargs={"slug": self.slug})
    
    def get_absolute_url_infouso(self):
        return reverse("mensagens:solicitaruso", kwargs={"slug": self.slug})

    def get_absolute_url_infoerro(self):
        return reverse("mensagens:informarerro", kwargs={"slug": self.slug})
    
    def get_absolute_url_editar(self):
        return reverse("bens:editbem", kwargs={"slug": self.slug})

#CALCULOS VIDA UTIL
    @property
    def dt_hoje(self):
        hoje = datetime.date.today()
        return hoje
#data inicial
    @property
    def dt_inicial(self):
        hoje = datetime.date.today()
        datainicial = self.data_inicial
        diff = hoje - datainicial
        days = diff.days
        months, days = days // 30, days

        return months

    @property
    def dt_final(self):
        #VIDA UTIL EM MESES
        informatica_veiculos = (int(60))
        maquinas_moveis = (int(120))
    
        

        #EQUIPAMENTOS DE INFORMATICA / VEICULOS
        if self.categoria.pk=="1819" or "2369":
            hoje = datetime.date.today()
            datainicial = self.data_inicial
            diff = hoje - datainicial
            days = diff.days
            months, days = days // 30, days
            adepreciar = informatica_veiculos - months
            if adepreciar<=0:
                return 0
            else:
                return adepreciar
                

        #MAQUINAS E EQUIPAMENTOS / MÓVEIS E UTENSILHOS 
        if self.categoria.pk=="1823" or "1821":
            hoje = datetime.date.today()
            datainicial = self.data_inicial
            diff = hoje - datainicial
            days = diff.days
            months, days = days // 30, days
            adepreciar = maquinas_moveis - months
            if adepreciar<=0:
                return 0
            else:
                return adepreciar

  
    
Product.objects.last
