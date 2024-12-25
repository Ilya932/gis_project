# Generated by Django 5.1.4 on 2024-12-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_place_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]