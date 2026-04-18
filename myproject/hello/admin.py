from django.contrib import admin
from .models import Service, Anggota

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('judul', 'ikon', 'status_aktif')
    list_editable = ('ikon',) 
    search_fields = ('judul',)
    
    # Memastikan tombol Save muncul di bagian atas juga
    save_on_top = True

    @admin.display(boolean=True, description='Status Aktif')
    def status_aktif(self, obj):
        return True 

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'email')
    list_filter = ('jabatan',)
    search_fields = ('nama', 'jabatan', 'email')
    ordering = ('nama',)
    
    # Fitur Update Objects Utama:
    # 1. Menampilkan tombol Save di bagian atas halaman edit
    save_on_top = True
    
    # 2. Menampilkan jumlah data yang dipilih saat melakukan bulk action
    show_full_result_count = True

    fieldsets = (
        ("Informasi Personal", {
            "fields": ("nama", "email"),
            "description": "Kelola informasi dasar identitas anggota tim."
        }),
        ("Detail Pekerjaan", {
            "fields": ("jabatan",),
            # 'wide' membuat tampilan input lebih lebar & rapi di Jazzmin
            # 'collapse' memungkinkan bagian ini disembunyikan
            "classes": ("collapse", "wide"), 
        }),
    )