# Generated by Django 4.2.3 on 2023-07-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='default_cover.jpg', upload_to=''),
        ),
    ]
