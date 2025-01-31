# Generated by Django 4.1.4 on 2023-02-10 12:28

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HHUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, max_length=30, verbose_name='Дата рождения')),
                ('city', models.CharField(blank=True, default='Unknown', max_length=180, verbose_name='Город')),
                ('gender', models.CharField(choices=[('U', 'Не определен'), ('F', 'Мужчина'), ('M', 'Женщина')], default='U', max_length=1, verbose_name='Пол')),
                ('patronymic', models.CharField(blank=True, max_length=124, null=True, verbose_name='Отчество')),
                ('is_company', models.BooleanField(default=False, help_text='Отметьте, если пользователь находится в роли работодателя', verbose_name='Является компанией')),
                ('is_candidate', models.BooleanField(default=False, help_text='Отметьте, если пользователь находится в роли соискателя', verbose_name='Является соискателем')),
                ('is_moderator', models.BooleanField(default=False, help_text='Отметьте, если пользователь находится в роли модератора', verbose_name='Является модератором')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
