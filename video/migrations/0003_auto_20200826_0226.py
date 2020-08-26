# Generated by Django 3.1 on 2020-08-26 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
        ('usuario', '0001_initial'),
        ('video', '0002_progresovideo_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='progresovideo',
            name='id_categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='curso.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='progresovideo',
            name='id_inscripcion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuario.inscripcion'),
            preserve_default=False,
        ),
    ]