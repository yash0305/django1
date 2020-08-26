from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm


def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered,'pending': pending}
    return render(request, 'home.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})

def createOrder(request):

    form = OrderForm()
    if request.method ==  'POST':
        #print('printing post:',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'order_form.html', {'form': form})

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()

    context = {'customer': customer, 'orders':orders}

    return render(request, 'customer.html', context)

