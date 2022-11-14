from django.shortcuts import render, get_object_or_404, redirect
from bens.models import Product
from django.contrib import messages
from .forms import UsoForm, ErroForm

# Create your views here.
def form_solicitaruso(request, slug):
    bem_solicitado = get_object_or_404(Product, slug=slug)    
    if request.method == "GET":
        
        uso = UsoForm(initial={'bem': bem_solicitado})
        

        context = {

            "uso": uso,
            "bem_solicitado": bem_solicitado,

        }
        

        return render(request, 'bens\solicitar_uso.html', context)

    elif request.method == "POST":
        
        uso = UsoForm(request.POST)
        

        if uso.is_valid():

            uso.save()
            
            messages.success(request, "SOLICITAÇÃO ENVIADA COM SUCESSO." ) 
            return redirect(bem_solicitado)
             
        else:
            context = {
                "uso": uso,
                
                
            }
            return render(request, 'bens\solicitar_uso.html', context)


def form_informarerro(request, slug):
    bem_solicitado = get_object_or_404(Product, slug=slug)    
    if request.method == "GET":
        
        erro_form = ErroForm(initial={'bem': bem_solicitado})
        

        context = {

            "erro_form": erro_form,
            "bem_solicitado": bem_solicitado,

        }
        

        return render(request, 'bens\informar_erro.html', context)

    elif request.method == "POST":
        
        erro_form = ErroForm(request.POST)
        

        if erro_form.is_valid():

            erro_form.save()
            messages.success(request, "INFORMAÇÃO ENVIADA COM SUCESSO." ) 
            return redirect(bem_solicitado)
        else:

            context = {
                "erro_form": erro_form,
                
                
            }
            return render(request, 'bens\informar_erro.html', context)