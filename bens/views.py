from django.shortcuts import  render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .models import Category, Product
from .forms import BensForm, ImagemForm
from django.db.models import Avg, Count, Min, Sum, Prefetch
from .filters import ListingFilter
import datetime


class ProductDetailView(DetailView):
    queryset = Product.available.all()
    

class ProductListView(ListView):
    category = None
   

    def get_queryset(self):
        queryset = Product.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            
            queryset = queryset.filter(categoria=self.category)
            
        return queryset

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()

        
        return context
        
#função editar bem  
def editBem(request, slug):
    messages.warning(request, "ATENÇÃO!!  MODO DE EDIÇÃO" )
    if request.method == "GET":
        bem = get_object_or_404(Product, slug=slug)
        form = BensForm(instance=bem)

        context = {
            "bem": bem,
            "form": form,

        }
        

        return render(request, 'bens\editbem.html', context)

    elif request.method == "POST":
        bem = get_object_or_404(Product, slug=slug)
        form = BensForm(request.POST,  request.FILES, instance=bem)

        if form.is_valid():
            form.save()
            messages.success(request, "SALVO COM SUCESSO!" )
            return redirect(bem)
        else:
            messages.error(request, "OCORREU ERRO, NÃO FOI SALVO..." )
            bem = get_object_or_404(Product, slug=slug)
            
            context = {
                "bem": bem,
                "form": form,
            }
            
            return render(request, 'bens\editbem.html', context)

#imagens_bens:
def imagemBem(request, slug):
    messages.warning(request, "ATENÇÃO!!  MODO DE EDIÇÃO" )
    if request.method == "GET":
        bem = get_object_or_404(Product, slug=slug)
        form = ImagemForm(instance=bem)

        context = {
            "bem": bem,
            "form": form,

        }
        

        return render(request, 'bens\imagembem.html', context)

    elif request.method == "POST":
        bem = get_object_or_404(Product, slug=slug)
        form = ImagemForm(request.POST,  request.FILES, instance=bem)

        if form.is_valid():
            form.save()
            messages.success(request, "SALVO COM SUCESSO!" )
            return redirect(bem)
        else:
            messages.error(request, "OCORREU ERRO, NÃO FOI SALVO..." )
            bem = get_object_or_404(Product, slug=slug)
            
            context = {
                "bem": bem,
                "form": form,
            }
            
            return render(request, 'bens\imagembem.html', context)
#função totais
def totais_list(request):
    
    saldos = Category.objects.annotate(qtd_bens=Count('products__slug')) 

    somas = Product.objects.aggregate(qt_total=Count('slug')) 


    context = {

        'saldos':saldos,
        'somas':somas,
    }
    
    return render(request, "bens/totais.html", context)


#função django-filters
def filtros_list(request):
    listings = Product.objects.all()

    listing_filter = ListingFilter(request.GET, queryset=listings)
    
    
    context = {
        'listing_filter': listing_filter
    }
    return render(request, "bens/filtros.html", context)