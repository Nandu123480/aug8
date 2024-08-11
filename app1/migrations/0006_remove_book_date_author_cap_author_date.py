# Generated by Django 5.0.7 on 2024-08-09 09:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.AddField(
            model_name='author',
            name='cap',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
