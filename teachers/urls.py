
from django.urls import path
from .import views

app_name = 'teachers'
urlpatterns = [
    path('',views.home, name="home"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.cart, name="checkout"),
    path('layout', views.layout, name="layout")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)