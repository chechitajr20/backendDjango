# Generated by Django 3.1.4 on 2020-12-12 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ('servicio',),
            },
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('costo', models.IntegerField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appservicios.cliente')),
                ('servicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appservicios.servicios')),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
    ]
