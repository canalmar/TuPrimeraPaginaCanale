from django.shortcuts import render, redirect
from .forms import ProductForm

def product_create(request):
    """ Vista para crear un nuevo producto.
    Si el request es POST: valida y guarda el producto, luego redirige.
    Si es GET: muestra el formulario vacío."""

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')  # Redirige a la lista de productos
    else:
        form = ProductForm()  # Formulario vacío para GET

    return render(request, 'product/product_form.html', {'form': form})


def product_list(request):
    """ Vista de lista de productos (temporal).
    Más adelante la completamos con la consulta y template correspondiente."""
    
    return render(request, 'product/product_list.html')



