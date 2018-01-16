# Generated by Django 2.0.1 on 2018-01-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afiliando', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ci',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='fecha_de_nacimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='matricula',
            field=models.PositiveIntegerField(),
        ),
    ]
