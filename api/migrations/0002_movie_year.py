# Generated by Django 4.2 on 2023-04-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
