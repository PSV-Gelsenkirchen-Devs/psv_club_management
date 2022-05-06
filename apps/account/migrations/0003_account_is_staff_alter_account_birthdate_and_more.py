# Generated by Django 4.0.1 on 2022-03-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_is_staff_account_is_board_account_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='birthdate',
            field=models.DateField(verbose_name='Geburstag'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Anmeldedatum'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name=' E-Mail'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Vorname'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktiv'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_board',
            field=models.BooleanField(default=False, verbose_name='Vorstand'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_coach',
            field=models.BooleanField(default=False, verbose_name='Trainer'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_member',
            field=models.BooleanField(default=True, verbose_name='Mitglied'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='SuperUser'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Letzter Login'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Nachname'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nutzername'),
        ),
    ]
