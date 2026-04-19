from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Service

class LatestServicesFeed(Feed):
    title = "TechGroup Innovation - Layanan Terbaru"
    link = "/services/"
    description = "Update terbaru mengenai solusi IoT dan pengembangan sistem dari TechGroup."

    # Mengambil 5 layanan terbaru
    def items(self):
        return Service.objects.all().order_by('-id')[:5]

    def item_title(self, item):
        return item.judul

    def item_description(self, item):
        return item.deskripsi

    # Link ke halaman detail yang sudah kita buat tadi
    def item_link(self, item):
        return reverse('service_detail', args=[item.id])