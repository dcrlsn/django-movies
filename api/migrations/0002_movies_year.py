# Generated by Django 4.0.6 on 2022-07-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='year',
            field=models.IntegerField(default=2000),
        ),
    ]
