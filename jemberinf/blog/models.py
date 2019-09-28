from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    judul       = models.CharField(max_length = 255)
    isi         = models.TextField()
    foto        = models.ImageField(default='default.jpg', upload_to='profile_pics')
    waktu       = models.DateTimeField(default = timezone.now)
    penulis     = models.ForeignKey(User, on_delete =  models.CASCADE)
    slug        = models.SlugField(blank = True, editable = False)

    def __str__(self):
        return self.judul

    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()

        img = Image.open(self.foto.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})