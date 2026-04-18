# hello/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Halaman Utama (Dashboard Mewah)
    path('', views.home, name='home'),
    
    # Halaman Informasi
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    
    # Halaman Redirect / Anggota
    path('anggota/', views.anggota, name='anggota'),
    
    # Halaman Kontak (Hanya satu baris saja, hapus duplikatnya)
    path('kontak/', views.kontak, name='kontak'),
]