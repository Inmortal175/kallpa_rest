# Generated by Django 4.0.3 on 2022-07-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0003_alter_presentacion_producto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion_producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='presentacion_producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
