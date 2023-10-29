# Generated by Django 4.2.6 on 2023-10-29 14:37

# Generated by Django 4.2.5 on 2023-10-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_username', models.CharField(default='author', max_length=150)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('data_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
