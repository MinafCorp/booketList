# Generated by Django 4.2.6 on 2023-12-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
