from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    products = Product.objects.all()

    total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,
    }

    return render(request, 'inventory/home.html', context)


def add_product(request):

    form = ProductForm()

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'inventory/add_product.html', context)

def update_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():

            form.save()

            return redirect('home')

    context = {
        'form': form
    }

    return render(
        request,
        'inventory/update_product.html',
        context
    )
    
def delete_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':

        product.delete()

        return redirect('home')

    context = {
        'product': product
    }

    return render(
        request,
        'inventory/delete_product.html',
        context
    )


        
        