from django.db import models

class Service(models.Model):
    judul = models.CharField(max_length=100, verbose_name="Nama Layanan")
    deskripsi = models.TextField(verbose_name="Deskripsi Layanan")
    # Ikon biasanya pake FontAwesome, CharField sudah pas
    ikon = models.CharField(max_length=50, help_text="Gunakan class FontAwesome (misal: fas fa-code)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name = "Layanan"
        verbose_name_plural = "Daftar Layanan"
        ordering = ['-created_at']


class Anggota(models.Model):
    # JABATAN_CHOICES ditingkatkan max_length-nya jadi 5 supaya aman
    JABATAN_CHOICES = [
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('DEV', 'Developer'),
        ('IOT', 'IoT Engineer'),
        ('DSN', 'Designer'),
    ]

    nama = models.CharField(max_length=100)
    # Gunakan max_length=5 untuk mengantisipasi kode jabatan yang lebih panjang
    jabatan = models.CharField(
        max_length=5, 
        choices=JABATAN_CHOICES, 
        default='DEV'
    )
    email = models.EmailField(blank=True, null=True)
    # Foto disatukan ke satu folder 'team/' agar rapi
    foto = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Upload foto profil tim")
    bio = models.TextField(blank=True, verbose_name="Biografi Singkat")

    def __str__(self):
        # Menggunakan get_jabatan_display() agar muncul nama lengkap jabatannya di Admin
        return f"{self.nama} - {self.get_jabatan_display()}"

    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Manajemen Anggota"
        ordering = ['nama']