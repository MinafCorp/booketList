# Generated by Django 4.2.6 on 2023-10-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_buku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(default=1, upload_to='book_images/'),
            preserve_default=False,
        ),
    ]