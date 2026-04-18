from django.db import models

class Service(models.Model):
    judul = models.CharField(max_length=100, verbose_name="Nama Layanan")
    deskripsi = models.TextField(verbose_name="Deskripsi Layanan")
    ikon = models.CharField(max_length=50, help_text="Gunakan class FontAwesome (misal: fas fa-code)")
    # Tambahkan tanggal input otomatis
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name = "Layanan"
        verbose_name_plural = "Daftar Layanan"
        ordering = ['-created_at'] # Layanan terbaru muncul di paling atas


class Anggota(models.Model):
    # Menggunakan pilihan (Choices) agar input jabatan seragam
    JABATAN_CHOICES = [
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('DEV', 'Developer'),
        ('IOT', 'IoT Engineer'),
        ('DSN', 'Designer'),
    ]

    nama = models.CharField(max_length=100)
    jabatan = models.CharField(
        max_length=3, 
        choices=JABATAN_CHOICES, 
        default='DEV'
    )
    email = models.EmailField(blank=True, null=True)
    # Mengaktifkan fitur foto
    foto = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Upload foto profil tim")
    bio = models.TextField(blank=True, verbose_name="Biografi Singkat")

    def __str__(self):
        return f"{self.nama} - {self.get_jabatan_display()}"

    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Manajemen Anggota"
        ordering = ['nama'] # Urutkan sesuai abjad nama