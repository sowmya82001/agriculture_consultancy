from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import contact_us, contact_success


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_consultant, name='book_consultant'),
    path('crops/', views.crop_recommendation, name='crop_recommendation'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='consultancy/login.html'), name='login'),
    path('book/success/', views.booking_success, name='booking_success'),  # Add this line
    path('contact/', contact_us, name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
]

