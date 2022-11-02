from django.shortcuts import  render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import Category, Product
from .forms import BensForm




class ProductDetailView(DetailView):
    queryset = Product.available.all()
    

class ProductListView(ListView):
    category = None
    paginate_by = 21

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
            return redirect(bem)
        else:
            bem = get_object_or_404(Product, slug=slug)

            context = {
                "bem": bem,
                "form": form,
            }
            return render(request, 'bens\editbem.html', context)



