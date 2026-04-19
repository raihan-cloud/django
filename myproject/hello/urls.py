# hello/urls.py
from django.urls import path
from . import views
from .feeds import LatestServicesFeed
urlpatterns = [
    # Halaman Utama (Dashboard Mewah)
    path('', views.home, name='home'),
    
    # Halaman Informasi
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:id>/', views.service_detail, name='service_detail'),
    path('post-comment-ajax/', views.post_comment_ajax, name='post_comment_ajax'),
    # Halaman Redirect / Anggota
    path('anggota/', views.anggota, name='anggota'),
    path('latest/rss/', LatestServicesFeed(), name='service_feed'),
    path('kontak/', views.kontak, name='kontak'),

    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('del-cookie/', views.delete_cookie, name='delete_cookie'),
    path('test-session/', views.test_session, name='test_session'),
    
    
]