# Generated by Django 4.1.5 on 2023-01-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game',
            field=models.ImageField(upload_to='images'),
        ),
    ]
