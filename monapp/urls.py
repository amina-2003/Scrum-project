from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listing/', views.listing, name='listing'),
    path('contact/', views.contact, name='contact'),
    path('recherche/', views.recherche_ajax, name='recherche_ajax'),
    path('category/', views.category_view, name='category'),        
    path("ajax/service/", views.recherche_par_service, name="recherche_par_service"),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail')
]