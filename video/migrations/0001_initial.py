# Generated by Django 3.1 on 2020-08-26 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgresoVideo',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('minutos_rep_diaria', models.IntegerField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
