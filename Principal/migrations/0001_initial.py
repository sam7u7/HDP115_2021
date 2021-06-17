# Generated by Django 3.2.3 on 2021-06-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('idAdministrador', models.AutoField(primary_key=True, serialize=False)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(primary_key=True, serialize=False)),
                ('DUI', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1)),
                ('numeroTelefono', models.CharField(max_length=50)),
                ('correoElectronico', models.EmailField(max_length=254)),
                ('rol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='zona',
            fields=[
                ('codigoZona', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('contrasena', models.CharField(max_length=50)),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.persona')),
            ],
        ),
        migrations.CreateModel(
            name='paqueteAlimentario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fechaDeExpedicion', models.DateField()),
                ('fechaDeCaducidad', models.DateField()),
                ('idAdministrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='asignacion',
            fields=[
                ('comprobante', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fechaDeAsignacion', models.DateField()),
                ('codigoZona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.zona')),
                ('idAdmistrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.administrador')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='administrador',
            name='idpersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.persona'),
        ),
    ]
