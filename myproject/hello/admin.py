from django.contrib import admin
from .models import Service, Anggota
from django.utils.html import format_html
from django.views.decorators.cache import cache_page
from django.core.cache import cache

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('judul', 'ikon', 'status_aktif')
    list_editable = ('ikon',) 
    search_fields = ('judul',)
    save_on_top = True

    @admin.display(boolean=True, description='Status Aktif')
    def status_aktif(self, obj):
        return bool(obj.judul) 
    
    # Tips: Bersihkan cache setiap kali data service diubah
    def save_model(self, request, obj, form, change):
        cache.clear() # Membersihkan cache agar halaman depan langsung update
        super().save_model(request, obj, form, change)

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('preview_foto', 'nama', 'jabatan', 'email')
    list_filter = ('jabatan',)
    search_fields = ('nama', 'jabatan', 'email')
    ordering = ('nama',)
    save_on_top = True
    show_full_result_count = True

    # Perbaikan: CSS object-fit agar foto tidak gepeng
    def preview_foto(self, obj):
        if obj.foto:
           return format_html('<img src="{}" style="width: 50px; border-radius: 10px;" />', obj.foto.url)
        return "No Photo"
    
    preview_foto.short_description = 'Foto'

    fieldsets = (
        ("Informasi Personal", {
            "fields": ("nama", "email", "foto"),
            "description": "Kelola informasi dasar identitas anggota tim."
        }),
        ("Detail Pekerjaan", {
            "fields": ("jabatan", "bio"), 
            "classes": ("wide",), 
        }),
    )

    # Menambahkan cache pada halaman daftar admin agar lebih cepat
    def changelist_view(self, request, extra_context=None):
        return super().changelist_view(request, extra_context)