# Generated by Django 3.1.1 on 2020-09-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0003_auto_20200919_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='soluong',
            field=models.IntegerField(default='1', verbose_name='Tồn kho'),
        ),
    ]
