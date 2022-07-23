# Generated by Django 4.0.3 on 2022-07-23 23:06

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile', models.ImageField(blank=True, upload_to='photos/profile')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('nombres', models.CharField(blank=True, max_length=255)),
                ('apellido_paterno', models.CharField(blank=True, max_length=255)),
                ('apellido_materno', models.CharField(blank=True, max_length=255)),
                ('documento_identidad', models.CharField(blank=True, max_length=8)),
                ('celular', models.CharField(blank=True, max_length=12)),
                ('kallpa_punto', models.CharField(blank=True, max_length=8)),
                ('origen_pais', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nac', models.DateTimeField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_egreso', models.DateTimeField(blank=True, null=True)),
                ('contrato', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('nombre_empresa', models.CharField(blank=True, max_length=255, null=True)),
                ('habilidades', models.TextField(blank=True, max_length=500)),
                ('es_validado', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('id_estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest.estado')),
                ('id_rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
