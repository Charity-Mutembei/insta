# Generated by Django 4.0.5 on 2022-06-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='', upload_to='posts'),
        ),
    ]