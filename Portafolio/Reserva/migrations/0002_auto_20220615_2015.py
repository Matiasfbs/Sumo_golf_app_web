# Generated by Django 3.1.2 on 2022-06-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.CharField(choices=[['consulta', 'consulta'], ['reclamo', 'reclamo'], ['sugerencia', 'sugerencia'], ['felicitaciones', 'felicitaciones']], max_length=20),
        ),
        migrations.AlterField(
            model_name='registro',
            name='dia',
            field=models.CharField(choices=[['Jueves', 'Jueves'], ['Viernes', 'Viernes']], max_length=50),
        ),
        migrations.AlterField(
            model_name='registro',
            name='lateralidad',
            field=models.CharField(choices=[['Diestro', 'DIESTRO'], ['Zurdo', 'ZURDO']], max_length=50),
        ),
        migrations.AlterField(
            model_name='registroreparacion',
            name='descripcion',
            field=models.TextField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='registroreparacion',
            name='fecha_recepcion',
            field=models.DateField(verbose_name='Fecha recepción'),
        ),
        migrations.AlterField(
            model_name='registroreparacion',
            name='precio',
            field=models.IntegerField(verbose_name='Costo reparación'),
        ),
        migrations.AlterField(
            model_name='registroreparacion',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name='Teléfono'),
        ),
    ]
