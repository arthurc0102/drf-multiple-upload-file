# Generated by Django 3.0.6 on 2020-05-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='uploads/%Y-%m-%d-%H-%M-%S/'),
        ),
    ]
