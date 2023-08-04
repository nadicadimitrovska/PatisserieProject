from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from .forms import CakesForm, CookiesForm, HealthyCookiesForm, SignUpForm, AddCakeForm, AddCookieForm, \
    AddHealthyCookieForm
from .models import Cakes, Cookies, HealthyCookies, Cart, CartItem


# Create your views here.


def patisserie(request):
    return render(request, "Pochetna.html")

def kontakt(request):
    return render(request, "Kontakt.html")

def zaNas(request):
    return render(request, "Za Nas.html")

def narachka(request):
    return render(request, "NarachkaPoZhelba.html")

@login_required
def shoppingCart(request):
    return render(request, "ShoppingCart.html")

def torti(request):
    queryset = Cakes.objects.all()
    context = {"cakes": queryset, "form": CakesForm}
    return render(request, "Torti.html", context=context)

def kolachi(request):
    queryset = Cookies.objects.all()
    context = {"cookies": queryset, "form": CookiesForm}
    return render(request, "Kolachi.html", context=context)

def prirodnaBaza(request):
    queryset = HealthyCookies.objects.all()
    context = {"healthy_cookies": queryset, "form": HealthyCookiesForm}
    return render(request, "PrirodnaBaza.html", context=context)

def cakeDetail(request,pk):
    cake = get_object_or_404(Cakes, pk=pk)
    return render(request, "CakesDetail.html", {'cake': cake})

def cookieDetail(request,pk):
    cookie = get_object_or_404(Cookies, pk=pk)
    return render(request, "CookieDetail.html", {'cookie': cookie})

def healthyCookieDetail(request,pk):
    healthyCookie = get_object_or_404(HealthyCookies, pk=pk)
    return render(request, "HealthyCookieDetail.html", {'healthyCookie': healthyCookie})

def delivery(request):
    return render(request, "Delivery.html")

def payment(request):
    return render(request, "Payment.html")

def successful(request):
    return render(request, "Successful.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def shopping_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0


    def get_product_details(product_model, product_id, quantity):
        try:
            product = product_model.objects.get(pk=product_id)
        except product_model.DoesNotExist:

            return None

        total_item_price = product.price * quantity
        return {
            'product': product,
            'product_id': product_id,
            'product_type': product_model.__name__.lower(),
            'quantity': quantity,
            'total_item_price': total_item_price,
        }


    for cookie_id, quantity in cart.get('cookies', {}).items():
        cookie_item = get_product_details(Cookies, cookie_id, quantity)
        if cookie_item:
            cart_items.append(cookie_item)
            total_price += cookie_item['total_item_price']


    for cake_id, quantity in cart.get('cakes', {}).items():
        cake_item = get_product_details(Cakes, cake_id, quantity)
        if cake_item:
            cart_items.append(cake_item)
            total_price += cake_item['total_item_price']


    for healthy_cookie_id, quantity in cart.get('healthycookies', {}).items():
        healthy_cookie_item = get_product_details(HealthyCookies, healthy_cookie_id, quantity)
        if healthy_cookie_item:
            cart_items.append(healthy_cookie_item)
            total_price += healthy_cookie_item['total_item_price']

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'ShoppingCart.html', context)


@login_required
def add_to_cart(request, product_id, product_type):
    quantity = int(request.POST.get('quantity', 1))


    if product_type not in ['cookies', 'cakes', 'healthycookies', ]:
        return HttpResponseBadRequest("Invalid product type")

    cart = request.session.get('cart', {})
    product_cart = cart.get(product_type, {})

    product_cart[str(product_id)] = product_cart.get(str(product_id), 0) + quantity

    cart[product_type] = product_cart

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('shopping_cart')


def update_cart(request):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_type = request.POST.get('product_type')
        action = request.POST.get('action')

        if product_type not in ['cookies', 'cakes', 'healthycookies',]:
            return HttpResponseBadRequest("Invalid product type")

        cart = request.session.get('cart', {})
        product_cart = cart.get(product_type, {})
        quantity = product_cart.get(str(product_id), 0)

        if action == 'increase':
            quantity += 1
        elif action == 'decrease':
            if quantity > 1:
                quantity -= 1
            else:

                del product_cart[str(product_id)]

        product_cart[str(product_id)] = quantity
        cart[product_type] = product_cart

        request.session['cart'] = cart
        request.session.modified = True


    return redirect('shopping_cart')


def remove_from_cart(request):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_type = request.POST.get('product_type')

        cart = request.session.get('cart', {})
        product_cart = cart.get(product_type, {})

        if str(product_id) in product_cart:
            del product_cart[str(product_id)]
            cart[product_type] = product_cart
            request.session['cart'] = cart
            request.session.modified = True

    return redirect('shopping_cart')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_HealthyCookie(request, healthy_cookie_id):
    healthyCookie = get_object_or_404(HealthyCookies, id=healthy_cookie_id)

    if request.method == 'POST':

        healthyCookie.title = request.POST['title']
        healthyCookie.ingredients = request.POST['ingredients']
        healthyCookie.price = request.POST['price']



        healthyCookie.save()

        return redirect('/prirodnaBaza', id=healthy_cookie_id)

    return render(request, 'editHealthyCookie.html', {'healthyCookie': healthyCookie})

@login_required
def delete_HealthyCookie(request, healthy_cookie_id):
    healthyCookie = get_object_or_404(HealthyCookies, id=healthy_cookie_id)

    if request.method == 'POST':
        healthyCookie.delete()
        return redirect('../../prirodnaBaza')

    return render(request, 'deleteHealthyCookie.html', {'healthyCookie': healthyCookie})

@login_required
def edit_cake(request, cake_id):
    # Get the cookie to be edited using the provided cookie_id
    cake = get_object_or_404(Cakes, id=cake_id)

    if request.method == 'POST':

        cake.title = request.POST['title']
        cake.ingredients = request.POST['ingredients']
        cake.price = request.POST['price']



        cake.save()

        return redirect('/torti', id=cake_id)

    return render(request, 'editCake.html', {'cake': cake})

@login_required
def delete_cake(request, cake_id):

    cake = get_object_or_404(Cakes, id=cake_id)

    if request.method == 'POST':

        cake.delete()
        return redirect('/torti')

    return render(request, 'deleteCake.html', {'cake': cake})


@login_required
def edit_cookie(request, cookie_id):

    cookie = get_object_or_404(Cookies, id=cookie_id)

    if request.method == 'POST':

        cookie.title = request.POST['title']
        cookie.ingredients = request.POST['ingredients']
        cookie.price = request.POST['price']



        cookie.save()

        return redirect('/kolachi', id=cookie_id)

    return render(request, 'editCookie.html', {'cookie': cookie})

@login_required
def delete_cookie(request, cookie_id):

    cookie = get_object_or_404(Cookies, id=cookie_id)

    if request.method == 'POST':

        cookie.delete()
        return redirect('/kolachi')

    return render(request, 'deleteCookie.html', {'cookie': cookie})

@login_required
def add_cake(request):
    if request.method == 'POST':
        form = AddCakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/torti')
    else:
        form = AddCakeForm()

    return render(request, 'AddCake.html', {'form': form})

def add_cookie(request):
    if request.method == 'POST':
        form = AddCookieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/kolachi')
    else:
        form = AddCakeForm()

    return render(request, 'AddCookie.html', {'form': form})



def add_healthycookie(request):
    if request.method == 'POST':
        form = AddHealthyCookieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/prirodnaBaza')
    else:
        form = AddHealthyCookieForm()

    return render(request, 'AddHealthyCookie.html', {'form': form})

def search_items(request):
    query = request.GET.get('q')
    cakes_results = Cakes.objects.filter(title__icontains=query) if query else []
    cookies_results = Cookies.objects.filter(title__icontains=query) if query else []
    healthy_cookies_results = HealthyCookies.objects.filter(title__icontains=query) if query else []

    return render(request, 'search_results.html', {
        'cakes_results': cakes_results,
        'cookies_results': cookies_results,
        'healthy_cookies_results': healthy_cookies_results,
        'query': query
    })







