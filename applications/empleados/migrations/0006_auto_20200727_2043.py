# Generated by Django 3.0.8 on 2020-07-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleados_other_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='other_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Otro Nombre'),
        ),
    ]
