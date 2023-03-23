from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import redirect_view


urlpatterns = [
    path('base', views.base, name='Base'),
    path('', views.main1, name='Main1'),
    path('main/', views.main, name='Main'),
    path('authorizd/', views.authorizd, name='authorizd'),
    #path('login', views.login , name= 'Login' ),
    path('auth/', views.auth, name='Auth'),
    path('main/category/<int:id_cat>', views.category, name='Category'),
    path('about/', views.about, name='about'),
    path('main/product/<int:id_prod>', views.product, name='Product'),
    path('redirect/', redirect_view),
    path('contact/', views.contact, name='Contact'),
    path('basket', views.basket, name='Basket'),
    path('forgot_password', views.forgot_password, name='Forgot_password')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
