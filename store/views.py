from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return HttpResponse("index")


def product_list(request):
    products = Product.available_products.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get('products', 2)
    products = paginator.page(page_number)

    context = {
        'products': products,
    }

    return render(request, 'store/list.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product.available_products, id=id)
    context = {
            'product': product,
        }
    
    return render(request, 'store/detail.html', context)
