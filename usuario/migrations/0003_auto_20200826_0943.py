# Generated by Django 3.1 on 2020-08-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200826_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]