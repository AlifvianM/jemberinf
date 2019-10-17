from django.contrib import admin
from .models import Post
# Register your models here.

# class PostAdmin(admin.ModelAdmin):
# 	readonly_fileds =[
# 			'judul',
# 			'isi',
# 			'kategori',
# 			'waktu_post',
# 			'foto',
# 			'penulis',
# 		]
		


admin.site.register( Post)
