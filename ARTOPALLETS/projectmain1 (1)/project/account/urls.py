from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from account.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('home', views.home, name='home'),
    path("gallery", TemplateView.as_view(template_name="gallery.html"), name='gallery'),
    path("about", TemplateView.as_view(template_name="about.html"), name='about'),
    path("service", TemplateView.as_view(template_name="services.html"), name='services'),
   
    path('login', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name="login"),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("buy", TemplateView.as_view(template_name="buy.html"), name='buy'),
    path("payment", TemplateView.as_view(template_name="payment.html"), name='payment'),
    path("sell", TemplateView.as_view(template_name="sell.html"), name='sell'),
    path("customization", views.customization, name='customization'),
    path("feedback", views.feedback, name='feedback'),
    path('payment_success/', views.payment_success, name='payment_success'),

]