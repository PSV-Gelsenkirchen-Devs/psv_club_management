# Generated by Django 4.0.1 on 2022-03-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oppclub',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Verein'),
        ),
        migrations.AlterField(
            model_name='oppplayer',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opponents.oppclub', verbose_name='Verein'),
        ),
        migrations.AlterField(
            model_name='oppplayer',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Vorname'),
        ),
        migrations.AlterField(
            model_name='oppplayer',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Nachname'),
        ),
    ]