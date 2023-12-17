# Generated by Django 4.2.5 on 2023-12-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.TextField(blank=True, null=True, verbose_name='Book-Title')),
                ('author', models.TextField(blank=True, null=True)),
                ('year_of_publication', models.IntegerField(blank=True, null=True, verbose_name='Year-Of-Publication')),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images/')),
            ],
        ),
    ]
