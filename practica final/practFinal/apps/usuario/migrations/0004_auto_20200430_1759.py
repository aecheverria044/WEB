# Generated by Django 3.0.5 on 2020-04-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='domicilio',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='repEnfermedad',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.TextField(max_length=1),
        ),
    ]
