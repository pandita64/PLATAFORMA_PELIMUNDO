# Generated by Django 5.0.6 on 2024-06-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misitio', '0007_configuracionsitio_remove_pelicula_imagen_fondo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_fondo_login', models.ImageField(blank=True, null=True, upload_to='imagenes_fondo_login')),
            ],
        ),
    ]
