# Generated by Django 4.2.6 on 2023-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_auto_20231027_1117'),
        ('user', '0002_remove_user_is_author_remove_user_is_reader_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ManyToManyField(to='book.book')),
                ('pengguna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='user.reader')),
            ],
        ),
    ]
