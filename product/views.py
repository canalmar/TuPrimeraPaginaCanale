from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages 

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
    """ Vista que muestra el listado de productos disponibles para gestión interna. """

    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def product_edit(request, product_id):
    """Permite editar un producto existente a través de un formulario.
    Si el método es POST, guarda los cambios.
    Si es GET, muestra el formulario con los datos actuales."""

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/product_form.html', {'form': form})

def product_delete(request, product_id):
    """Vista para eliminar un producto.
    Muestra confirmación previa si es GET. Elimina si es POST."""

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('product:product_list')

    return render(request, 'product/product_confirm_delete.html', {'product': product})








