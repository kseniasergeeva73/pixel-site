# Generated by Django 3.2.19 on 2023-06-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=None, upload_to='media/'),
        ),
    ]