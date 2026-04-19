from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse # Ditambahkan JsonResponse untuk AJAX
from django.contrib.contenttypes.models import ContentType
from django_comments.models import Comment

from .forms import KontakForm
from .models import Anggota, Service

def home(request):
    semua_service = Service.objects.all()
    return render(request, "home.html", {"services": semua_service})

def anggota(request):
    data_anggota = Anggota.objects.all().order_by('nama')
    return render(request, "team.html", {"anggota": data_anggota})

def kontak(request):
    if request.method == 'POST':
        form = KontakForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            email_pengirim = form.cleaned_data['email']
            pesan = form.cleaned_data['pesan']

            try:
                send_mail(
                    f'Notifikasi TechGroup dari {nama}',
                    f'Pesan: {pesan}\n\nDari: {email_pengirim}',
                    settings.EMAIL_HOST_USER,
                    ['admin@techgroup.id'],
                    fail_silently=False,
                )
                messages.success(request, f"Terima kasih {nama}, pesan Anda terkirim!")
            except Exception as e:
                # Mode Dev: Tetap beri feedback meski email belum dikonfigurasi
                messages.info(request, "Pesan diterima (Mode Pengembangan).")
            
            return redirect('home')
    else:
        form = KontakForm()
    return render(request, "kontak.html", {'form': form})

def about(request):
    data_anggota = Anggota.objects.all()
    return render(request, "about.html", {"anggota": data_anggota})

def services(request):
    semua_service = Service.objects.all()
    return render(request, "services.html", {"services": semua_service})

def service_detail(request, id):
    # Menggunakan get_object_or_404 agar jika ID salah, muncul 404 bukan error kode
    service = get_object_or_404(Service, id=id)
    return render(request, "service_detail.html", {"object": service})

# --- FUNGSI AJAX BARU ---
def post_comment_ajax(request):
    if request.method == "POST":
        nama = request.POST.get('name')
        email = request.POST.get('email')
        isi_komentar = request.POST.get('comment')
        object_id = request.POST.get('object_pk')

        if nama and isi_komentar:
            # Simpan komentar ke database
            # Catatan: ContentType digunakan untuk menghubungkan komentar ke model Service
            ctype = ContentType.objects.get_for_model(Service)
            new_comment = Comment.objects.create(
                user_name=nama,
                user_email=email,
                comment=isi_komentar,
                object_pk=object_id,
                content_type=ctype,
                site_id=settings.SITE_ID
            )

            return JsonResponse({
                "status": "success",
                "name": new_comment.user_name,
                "comment": new_comment.comment,
            })
    return JsonResponse({"status": "error"}, status=400)

# --- COOKIES & SESSIONS ---
def set_cookie(request):
    response = HttpResponse("<h1>TechGroup: Cookie telah dipasang!</h1>")
    response.set_cookie('user_visitor', 'Raihan', max_age=3600)
    return response

def get_cookie(request):
    nama_pengunjung = request.COOKIES.get('user_visitor', 'Tamu')
    return render(request, 'hello_cookie.html', {'nama': nama_pengunjung})

def delete_cookie(request):
    response = HttpResponse("<h1>TechGroup: Cookie telah dihapus!</h1>")
    response.delete_cookie('user_visitor')
    return response

def test_session(request):
    jumlah_kunjungan = request.session.get('kunjungan', 0)
    request.session['kunjungan'] = jumlah_kunjungan + 1
    return render(request, 'session_view.html', {'count': request.session['kunjungan']})

def clear_session(request):
    request.session.flush()
    return HttpResponse("<h1>Session telah dibersihkan!</h1>")

def error_404_view(request, exception):
    return render(request, '404.html', status=404)