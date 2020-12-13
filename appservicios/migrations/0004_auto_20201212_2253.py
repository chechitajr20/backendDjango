# Generated by Django 3.1.4 on 2020-12-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appservicios', '0003_auto_20201212_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratos',
            name='clientes',
        ),
        migrations.AddField(
            model_name='contratos',
            name='clientes',
            field=models.ManyToManyField(to='appservicios.Cliente'),
        ),
        migrations.RemoveField(
            model_name='contratos',
            name='servicios',
        ),
        migrations.AddField(
            model_name='contratos',
            name='servicios',
            field=models.ManyToManyField(to='appservicios.Servicios'),
        ),
    ]
