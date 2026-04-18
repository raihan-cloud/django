from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')), 
]

# Handler untuk halaman error 404
handler404 = 'hello.views.error_404_view'

# Melayani file static & media saat pengembangan (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Tambahkan ini juga jika kamu menggunakan folder media untuk upload foto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)