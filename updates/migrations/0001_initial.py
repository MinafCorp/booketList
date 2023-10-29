
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
