# Generated by Django 3.0.5 on 2020-04-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('pais', models.TextField()),
                ('ciudad', models.TextField()),
                ('domicilio', models.TextField()),
                ('sexo', models.TextField()),
                ('edad', models.IntegerField()),
                ('areamedica', models.TextField()),
                ('repEnfermedad', models.TextField()),
                ('duracion', models.TextField()),
                ('comentarios', models.TextField()),
                ('contraseña', models.TextField()),
            ],
        ),
    ]