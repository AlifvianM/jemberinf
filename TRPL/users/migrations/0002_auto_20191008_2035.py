# Generated by Django 2.2.3 on 2019-10-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='profile_pics'),
        ),
    ]
