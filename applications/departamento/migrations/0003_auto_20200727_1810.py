# Generated by Django 3.0.8 on 2020-07-27 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20200726_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]