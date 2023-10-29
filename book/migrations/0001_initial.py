

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.TextField(blank=True, null=True, verbose_name='Book-Title')),
                ('author', models.TextField(blank=True, null=True)),
                ('year_of_publication', models.IntegerField(blank=True, null=True, verbose_name='Year-Of-Publication')),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image_url_s', models.URLField(blank=True, null=True, verbose_name='Image-URL-S')),
                ('image_url_m', models.URLField(blank=True, null=True, verbose_name='Image-URL-M')),
                ('image_url_l', models.URLField(blank=True, null=True, verbose_name='Image-URL-L')),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_rating', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
