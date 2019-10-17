from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	KATEGORI = (
			('Jalan', 'jalan'),
			('Jembatan', 'jembatan'),
			('Lampu Jalan', 'lampu_jalan'),
		)

	STATUS = (
			('Belum Di Survey', 'belum_di_survey'),
			('Sedang Di Survey', 'sedang_di_survey'),
			('Telah Di Survey', 'telah_di_survey'),
			('Dalam Proses Pengerjaan','dalam_proses_pengerjaan'),
			('Telah Di Perbaiki', 'telah_di_perbaiki') 
		)

	judul		= models.CharField(max_length=255)
	isi 		= models.TextField()
	kategori 	= models.CharField(max_length=255, choices=KATEGORI)
	waktu_post	= models.DateTimeField(default=timezone.now)
	foto 		= models.ImageField(default='blank.jpg', upload_to='pengaduan', null=True, blank=True)
	status 		= models.CharField(max_length=255, choices=STATUS, default='Belum Di Survey')
	penulis		= models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.judul
		

	def save(self):
		super().save()

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.pk})