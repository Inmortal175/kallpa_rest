# Generated by Django 4.0.3 on 2022-07-23 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_rest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='productopersonalizado',
            name='client_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productopersonalizado',
            name='dispositivo_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.dispositivo'),
        ),
        migrations.AddField(
            model_name='productopersonalizado',
            name='marca_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.marca'),
        ),
        migrations.AddField(
            model_name='productopersonalizado',
            name='modelo_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.modelo'),
        ),
        migrations.AddField(
            model_name='productopersonalizado',
            name='precio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest.precioproductopersonalizado'),
        ),
        migrations.AddField(
            model_name='productopersonalizado',
            name='tipo_producto_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.tipo_producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='dispositivo_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.dispositivo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='evento_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.evento'),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.marca'),
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.modelo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='presentacion_Producto_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.presentacion_producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.tipo_producto'),
        ),
        migrations.AddField(
            model_name='precioproductopersonalizado',
            name='Empleado_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='precioproductopersonalizado',
            name='dispositivo_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.dispositivo'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='id_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.marca'),
        ),
        migrations.AddField(
            model_name='marca',
            name='id_dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.dispositivo'),
        ),
        migrations.AddField(
            model_name='imagenproductopersonalizado',
            name='ProductoPersonalizado_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.productopersonalizado'),
        ),
        migrations.AddField(
            model_name='imagenes_producto',
            name='Presentacion_Producto_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.presentacion_producto'),
        ),
    ]
