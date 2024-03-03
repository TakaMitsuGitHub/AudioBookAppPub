# Generated by Django 5.0.1 on 2024-03-03 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_rename_audio_audiobookmodel'),
        ('book', '0003_rename_book_bookmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobookmodel',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.bookmodel'),
        ),
    ]