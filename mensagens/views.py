from django.shortcuts import render, get_object_or_404, redirect
from bens.models import Product
from .models import Uso, Erro
from .forms import UsoForm, ErroForm

# Create your views here.
def form_solicitaruso(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        uso = UsoForm(request.POST)
        # check whether it's valid:
        if uso.is_valid():
            # process the data in form.cleaned_data as required
            
            uso.save()
            uso = UsoForm()
            
            # ...
            # redirect to a new URL:
            return render(request, "bens/solicitar_uso.html", {"uso": uso})

    # if a GET (or any other method) we'll create a blank form
    else:
        uso = UsoForm()

    return render(request, "bens/solicitar_uso.html", {"uso": uso})

def form_informarerro(request):
        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        erro = ErroForm(request.POST)
        # check whether it's valid:
        if erro.is_valid():
            # process the data in form.cleaned_data as required
            erro.save()
            erro = ErroForm()
            # ...
            # redirect to a new URL:
            return render(request, "bens/informar_erro.html", {"erro": erro})

    # if a GET (or any other method) we'll create a blank form
    else:
        erro = ErroForm()

    return render(request, "bens/informar_erro.html", {"erro": erro})
