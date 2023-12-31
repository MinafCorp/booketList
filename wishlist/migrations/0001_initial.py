# Generated by Django 4.2.5 on 2023-12-13 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ManyToManyField(related_name='wishlists', to='book.book')),
                ('pengguna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='user.reader')),
            ],
        ),
    ]
