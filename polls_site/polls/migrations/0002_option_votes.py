# Generated by Django 3.1.3 on 2020-11-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
