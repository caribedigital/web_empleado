# Generated by Django 3.0.8 on 2020-07-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20200727_1810'),
        ('empleados', '0002_auto_20200726_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AddField(
            model_name='empleados',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'ABOGADO'), ('4', 'OTRO')], max_length=50, verbose_name='Trabajo'),
        ),
        migrations.AlterUniqueTogether(
            name='empleados',
            unique_together={('first_name', 'departamento')},
        ),
    ]
