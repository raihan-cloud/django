from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    # Cukup render satu file, misalnya 'home.html'
    return render(request, "home.html")

def anggota(request):
    # Langsung lempar ke home tanpa halaman perantara
    return redirect('home')

def kontak(request):
    if request.method == 'POST':
        nama = request.POST.get('nama', 'User')
        try:
            send_mail(
                f'Notifikasi TechGroup dari {nama}',
                'Seseorang menghubungi via form kontak.',
                settings.EMAIL_HOST_USER,
                ['admin@techgroup.id'],
                fail_silently=False,
            )
        except:
            pass # Abaikan jika email gagal agar tidak error 500
        
        # Selesai kirim, langsung balik ke home
        return redirect('home')
        
    return render(request, "kontak.html", {})

def about(request):
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})

# Tambahkan ini di bagian paling bawah hello/views.py
def error_404_view(request, exception):
    return render(request, '404.html', status=404)