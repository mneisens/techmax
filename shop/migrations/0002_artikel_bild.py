# Generated by Django 5.1.7 on 2025-03-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='bild',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
