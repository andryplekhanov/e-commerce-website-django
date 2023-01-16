# Generated by Django 4.1.3 on 2023-01-12 17:59

import app_users.managers
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroups',
            fields=[
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('full_name', models.CharField(blank=True, max_length=255, verbose_name='ФИО')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='является активным')),
                ('is_staff', models.BooleanField(default=False, verbose_name='является сотрудником')),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79012345678'.", regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')], verbose_name='номер телефона')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', app_users.managers.UserManager()),
            ],
        ),
    ]
