# Generated by Django 4.1.3 on 2022-11-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_alter_jugadores_num_dorsal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='num_dorsal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
