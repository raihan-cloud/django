from django import forms

class KontakForm(forms.Form):
    nama = forms.CharField(max_length=100, label="Nama Lengkap")
    email = forms.EmailField(label="Alamat Email")
    pesan = forms.CharField(widget=forms.Textarea, label="Isi Pesan")

