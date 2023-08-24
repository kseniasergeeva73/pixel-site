from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'app'
urlpatterns = [
    path('', views.render_index, name='index'),
    path('products/<int:category_id>/', views.render_products, name='products'),
    path('shopping_cart/<str:username>/', views.render_shopping_cart, name='shopping_cart'),
    path('shopping_cart/<str:username>/add/<int:product_id>/', views.add_product_to_shopping_cart, name='add_product'),
    path('shopping_cart/<str:username>/remove/<int:product_id>/', views.remove_product_from_shopping_cart, name='remove_product'),
    path('about/', views.render_about, name='about'),
    path('contact/', views.render_contact, name='contact'),
    path('delivery/', views.render_delivery, name='delivery'),
    path('guarantee/', views.render_guarantee, name='guarantee'),
    path('return/', views.render_return, name='return'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]