"""PatisserieProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Patisserie.views import patisserie, torti, kolachi, prirodnaBaza, kontakt, zaNas, narachka, shoppingCart, \
    cakeDetail, cookieDetail, healthyCookieDetail, \
    delivery, payment, successful, shopping_cart, add_to_cart, update_cart, remove_from_cart, signup, profile, \
    edit_cake, delete_cake, edit_HealthyCookie, delete_HealthyCookie, edit_cookie, delete_cookie, add_cake, add_cookie, \
    add_healthycookie, search_items
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patisserie/', patisserie, name="patisserie"),
    path('torti/', torti, name="torta"),
    path('kolachi/', kolachi, name="kolach"),
    path('prirodnaBaza/', prirodnaBaza, name="prirodnaBaza"),
    path('kontakt/', kontakt, name="kontakt"),
    path('zaNas/', zaNas, name="zaNas"),
    path('narachka/', narachka, name="narachka"),
    path('shoppingCart/', shoppingCart, name="shoppingCart"),
    path('cakeDetail/<int:pk>/', cakeDetail, name="cakeDetail"),
    path('cookieDetail/<int:pk>/', cookieDetail, name="cookieDetail"),
    path('healthyCookieDetail/<int:pk>/', healthyCookieDetail, name="healthyCookieDetail"),
    path('delivery/', delivery, name="delivery"),
    path('payment/', payment, name="payment"),
    path('successful/', successful, name="successful"),
    path('add_to_cart/<int:product_id>/<str:product_type>/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('signup/', signup, name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('edit/<int:healthy_cookie_id>/', edit_HealthyCookie, name='edit_HealthyCookie'),
    path('delete/<int:healthy_cookie_id>/', delete_HealthyCookie, name='delete_HealthyCookie'),
    path('editCake/<int:cake_id>/', edit_cake, name='edit_cake'),
    path('deleteCake/<int:cake_id>/', delete_cake, name='delete_cake'),
    path('editCookie/<int:cookie_id>/', edit_cookie, name='edit_cookie'),
    path('deleteCookie/<int:cookie_id>/', delete_cookie, name='delete_cookie'),
    path('add_cake/', add_cake, name='add_cake'),
    path('add_cookie/', add_cookie, name='add_cookie'),
    path('add_healthycookie/', add_healthycookie, name='add_healthycookie'),
    path('search/', search_items, name='search_items'),

    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/', views.cart, name='cart'),

   path('accounts/', include('django.contrib.auth.urls')),

    # path('order/', orders, name="order"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
