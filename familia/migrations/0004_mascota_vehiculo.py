# Generated by Django 4.0.4 on 2022-05-31 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0003_persona_altura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=100)),
                ('dueño', models.CharField(max_length=100)),
            ],
        ),
    ]
