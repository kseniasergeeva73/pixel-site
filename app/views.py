from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from django.views.generic import View
from .models import *

def render_index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'is_main':True,
    })

def render_shopping_cart(request, username):
    categories = Category.objects.all()
    user = User.objects.get(username=username)
    shopping_cart = ShoppingCart.objects.get(user=user)
    price_all = 0
    for i in shopping_cart.products.all():
        price_all += i.price
    return render(request, 'shopping_cart.html', {
        'categories': categories,
        'shopping_cart': shopping_cart,
        'price_all': price_all,
    })

def add_product_to_shopping_cart(request, username, product_id):
    user = User.objects.get(username=username)
    shopping_cart = ShoppingCart.objects.get(user=user)
    product = Product.objects.get(id=product_id)
    shopping_cart.products.add(product)
    
    return render_products(request, product.category.id)

def remove_product_from_shopping_cart(request, username, product_id):
    user = User.objects.get(username=username)
    shopping_cart = ShoppingCart.objects.get(user=user)
    product = Product.objects.get(id=product_id)
    shopping_cart.products.remove(product)

    return render_shopping_cart(request, username)

def render_products(request, category_id):
    categories = Category.objects.all()
    try:
        products = Product.objects.filter(category_id=category_id)
    except:
        products = None
    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'is_main':False,
    })

def render_about(request):
    categories = Category.objects.all()
    return render(request, 'about.html', {
        'categories': categories,
    })

def render_contact(request):
    categories = Category.objects.all()
    return render(request, 'contact.html', {
        'categories': categories,
    })

def render_delivery(request):
    categories = Category.objects.all()
    return render(request, 'delivery.html', {
        'categories': categories,
    })

def render_guarantee(request):
    categories = Category.objects.all()
    return render(request, 'guarantee.html', {
        'categories': categories,
    })

def render_return(request):
    categories = Category.objects.all()
    return render(request, 'return.html', {
        'categories': categories,
    })

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        return render(request, 'login.html', {'form':form, 'categories': categories})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form':form})


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        categories = Category.objects.all()
        return render(request, 'registration.html', {'form':form, 'categories': categories})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {'form':form})