# Generated by Django 3.2 on 2021-05-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_image_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='code',
            field=models.CharField(default='empty', max_length=12),
        ),
    ]