# Generated by Django 4.0.1 on 2022-03-03 18:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0002_gamemodel_home_gamemodel_points_opponents_and_more'),
        ('teams', '0002_alter_teammodel_name_alter_teammodel_player_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamModel',
            new_name='Team',
        ),
    ]